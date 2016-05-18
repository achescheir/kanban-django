var apiUrl = '/api/tasks/'
$( ".connectedSortable" ).sortable({
  connectWith: ".connectedSortable"
});
$( ".tasks" ).disableSelection();
$( ".connectedSortable" ).droppable({
  // drop:console.log("hello")
  drop: handleDrop
});
function handleDrop(event, ui){
  console.log(ui.draggable)
  console.log(ui.draggable.next())
};

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
$("#taskForm").submit(function(e){
  e.preventDefault();

  console.log('trying to submit')

  var form = new FormData();
  form.append("title", $("#id_title").val());
  form.append("status", $("#id_status").val());
  form.append("priority", $("#id_priority").val());

  console.log(form)

  var settings = {
    "async": true,
    "crossDomain": true,
    "url": apiUrl,
    "method": "POST",
    "headers": {
      "cache-control": "no-cache",
      "X-CSRFToken": csrftoken,
    },
    "processData": false,
    "contentType": false,
    "mimeType": "multipart/form-data",
    "data": form
  }

  $.ajax(settings).done(function (response) {
    console.log(response);
  });

})
