var form = document.getElementById('form'),
  submit = document.getElementById('submit'),
  addAddress = document.getElementById('addAddress'),
  addAddressEnd = document.getElementById('addAddressEnd'),
  resultDiv = document.getElementById('result'),
  imagesDownAddress = document.getElementById('images-down-address'),
  imagesDown = document.getElementById('images-down');

var data = {};

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

addAddress.addEventListener('click', function() {
  var input = document.createElement('input');
  input.setAttribute('type', 'text');
  input.setAttribute('name', 'pageAddress');
  input.setAttribute('value', 'http://');
  form.insertBefore(input, addAddressEnd);
});

submit.addEventListener('click', function() {
  submit.disabled = true;
  var data = serializeForm(form);
  ajax.post('connect.py', data, result);
});

imagesDown.addEventListener('click', function() {
  imagesDown.disabled = true;
  var imagesdata = serializeImages(data.images);
  ajax.post('images_down.py', imagesdata, imagesResult);
});

function result(e) {
  data.images = [];
  try {
    var result = JSON.parse(e);
    for (var i of result) {
      for (var index in i.images) {
        data.images.push(i.images[index]);
      }
      _createDom(i, resultDiv);
    }
    imagesDown.disabled = false;
  } catch (err) {
    console.log('nojsoon');
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
      _createElementHaveClass('p', 'url', info.url, itemHead);
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
  }
}

function serializeForm(form) {
  var setForm = '';
  for (var key in form) {
    if (form.hasOwnProperty(key) && form[key].name != '') {
      if (form[key].name == 'common') {
        data.common = form[key].value;
      }
      setForm += encodeURIComponent(form[key].name) + '=' + encodeURIComponent(form[key].value) + '&';
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