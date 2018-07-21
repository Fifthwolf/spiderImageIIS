var mainForm = $('main-form'),
  submit = $('submit'),
  reset = $('reset'),
  addAddressEnd = $('addAddressEnd'),
  common = $('common'),
  distinguish = $('distinguish'),
  resultDiv = $('result'),
  quickSubmit = $('quickSubmit'),
  pageNum = $('pageNum'),
  imagesDownAddress = $('images-down-address'),
  imagesDown = $('images-down');

var data = {
  'images': []
};

var ajax = {
  post: function(url, data, fn) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 304)) {
        fn.call(this, xhr.responseText);
      }
    };
    xhr.send(data);
  }
}

submit.addEventListener('click', function() {
  var data = serializeForm(mainForm);
  ajax.post('connect.py', data, result);
});

distinguish.addEventListener('click', function() {
  const data = [
    [/acfun\.cn\/a\/ac\d+/, 1],
    [/bilibili\.com\/read\/cv\d+/, 2],
    [/h\.bilibili\.com\/\d+/, 3],
    [/zhihu\.com\/question\/\d+\/answer\/\d+/, 4],
    [/pixiv\.net\/member_illust\.php\?.*illust_id=\d+/, 5],
  ];

  var website = mainForm.pageAddress.value.split('\n')[0];

  for (var i = 0, len = data.length; i < len; i++) {
    if (data[i][0].test(website)) {
      common.value = data[i][1];
      break;
    }
  }
});

reset.addEventListener('click', resetFunc);

quickSubmit.addEventListener('click', function(e) {
  const data = [{
    'pageAddress': 'https://h.bilibili.com/d',
    'common': '3_1'
  }, {
    'pageAddress': 'https://h.bilibili.com/d',
    'common': '3_2'
  }, {
    'pageAddress': 'https://h.bilibili.com/d',
    'common': '3_3'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/illustration/hot',
    'common': '3_4'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/illustration/new',
    'common': '3_5'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/comic/hot',
    'common': '3_6'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/comic/new',
    'common': '3_7'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/other/hot',
    'common': '3_8'
  }, {
    'pageAddress': 'https://h.bilibili.com/eden/draw_area#/other/new',
    'common': '3_9'
  }]

  if (e.target.type == 'button') {
    var index = e.target.getAttribute('data-id') - 1;
    ajax.post('connect.py', quickSerializeObject(data[index]), quickSubmitResult);
  }
});

function quickSerializeObject(obj) {
  var setForm = '';
  for (var i in obj) {
    setForm += encodeURIComponent(i) + '=' + encodeURIComponent(obj[i]) + '&';
  }
  var pageIndex = parseInt(pageNum.value);
  if (pageIndex != NaN && pageIndex > 0) {
    setForm += 'pageNum=' + (pageIndex - 1);
  } else {
    setForm += 'pageNum=0';
  }
  return setForm;
}

function quickSubmitResult(e) {
  var itmes = [];
  try {
    var jsondata = JSON.parse(e);
    for (var i of jsondata) {
      for (var index in i.images) {
        itmes.push([i.images[index], i.title]);
      }
    }
  } catch (err) {
    console.log(err);
  }

  ajax.post('connect.py', _serialize(itmes), result);

  function _serialize(itmes) {
    var setForm = '';
    for (var i of itmes) {
      setForm += 'pageAddress=' + encodeURIComponent('https://h.bilibili.com/') + i[0] + '&';
    }
    setForm += 'common=3'
    return setForm;
  }
}

imagesDown.addEventListener('click', function() {
  imagesDown.innerHTML = '下载中';
  imagesDown.disabled = true;
  reset.disabled = true;
  var imagesdata = serializeImages(data.images);
  ajax.post('images_down.py', imagesdata, imagesResult);
});

function resetFunc() {
  data = {};
  submit.disabled = false;
  imagesDown.disabled = true;

  //页面地址栏清空
  pageAddressInput = mainForm.getElementsByClassName('pageAddress');
  for (var i = pageAddressInput.length - 1; i >= 1; i--) {
    mainForm.removeChild(pageAddressInput[i]);
  }

  //结果清空
  resultItem = resultDiv.getElementsByClassName('item');
  for (var i = resultItem.length - 1; i >= 0; i--) {
    resultDiv.removeChild(resultItem[i]);
  }
}

function result(e) {
  try {
    var result = JSON.parse(e);
    for (var i of result) {
      for (var index in i.images) {
        data.images.push([i.images[index], i.title]);
      }
      _createDom(i, resultDiv);
    }
    imagesDown.disabled = false;
  } catch (err) {
    console.log(err);
  }

  function _createDom(info, parent) {
    var item = _createElementHaveClass('div', 'item', '', parent)
    _createHead(info, item);
    if (info.title != '无效地址') {
      _createImgwrapper(info, item);
    }

    function _createHead(info, parent) {
      var itemHead = _createElementHaveClass('div', 'item-head', '', parent);
      _createElementHaveClass('p', 'title', info.title, itemHead);
      _createElementHaveClass('a', 'url', '<a href="' + info.url + '">' + info.url + '</a>', itemHead);
    }

    function _createImgwrapper(info, parent) {
      var imgWrapper = _createElementHaveClass('div', 'img-wrapper', '', parent);
      for (var image of info.images) {
        var img = document.createElement('img');
        img.setAttribute('src', image);
        imgWrapper.appendChild(img);
      }
    }

    function _createElementHaveClass(type, className, content, parent) {
      var ele = document.createElement(type);
      ele.setAttribute('class', className);
      ele.innerHTML = content;
      parent.appendChild(ele);
      return ele;
    }
  }
}

function imagesResult(e) {
  if (e == 1) {
    alert('下载成功！');
    imagesDown.innerHTML = '下载成功';
    imagesDown.disabled = false;
    reset.disabled = false;
  }
}

function serializeForm(form) {
  var setForm = '';
  for (var key in form) {
    if (form.hasOwnProperty(key) && form[key].name != '') {
      switch (form[key].name) {
        case 'pageAddress':
          let pageValues = form[key].value.split('\n');
          for (var i = 0, len = pageValues.length; i < len; i++) {
            setForm += encodeURIComponent(form[key].name) + '=' + encodeURIComponent(pageValues[i]) + '&';
          }
          break;
        case 'common':
          data.common = form[key].value;
          setForm += encodeURIComponent(form[key].name) + '=' + encodeURIComponent(form[key].value) + '&';
          break;
      }
    }
  }
  return setForm.slice(0, setForm.length - 1);
}

function serializeImages(images) {
  var imagesdata = '';
  for (var i = 0; i < images.length; i++) {
    imagesdata += 'images=' + encodeURIComponent(images[i]) + '&';
  }
  imagesdata += 'path=' + encodeURIComponent(imagesDownAddress.value);
  return imagesdata;
}

function $(id) {
  return document.getElementById(id);
}
