var form = document.getElementById('form'),
  submit = document.getElementById('submit');
resultDiv = document.getElementById('result');

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
  var data = serializeForm(form);
  ajax.post('connect.py', data, result);
});

function result(e) {
  // try {
  //   var result = JSON.parse(e);
  //   for (var i of result) {
  //     _createDom(i, resultDiv);
  //   }
  // } catch (err) {
  //   console.log('nojsoon');
  // }
  var result = JSON.parse(e);
  for (var i of result) {
    console.log(i);
    try {
      _createDom(i, resultDiv);
    } catch (err) {
      console.log('nodiv');
    }
  }

  function _createDom(info, parent) {
    var item = _createElementHaveClass('div', 'item', '', parent)

    _createHead(info, item);
    _createImgwrapper(info, item);

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

function serializeForm(form) {
  var setForm = '';
  for (var key in form) {
    if (form.hasOwnProperty(key) && form[key].name != '') {
      setForm += encodeURIComponent(form[key].name) + '=' + encodeURIComponent(form[key].value) + '&';
    }
  }
  return setForm.slice(0, setForm.length - 1);
}