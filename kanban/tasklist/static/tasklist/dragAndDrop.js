$( ".connectedSortable" ).sortable({
  connectWith: ".connectedSortable"
});
$( ".tasks" ).disableSelection();
$( ".connectedSortable" ).droppable({
  // drop:console.log("hello")
  drop: handleDrop
});
function handleDrop(event, ui){
    console.log($(ui.draggable))
    console.log($(ui.draggable.next('li')))
  };
