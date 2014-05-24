function setDirectory(iter)
{
	var name = '.hFinderDirectory';
	name += iter;
	obj = $(name);
	obj.draggable({containment: "#hFinderFiles",scroll:false});
}
$(document).ready(
	function() {
		$('#dropzone').droppable({
			drop: function(event, ui) {
				$(this).css('background-color','pink');
			}
		});
		setDirectory(1);
		setDirectory(2);
		setDirectory(3);
		setDirectory(4);
		setDirectory(5);
		setDirectory(6);
		setDirectory(7);
		setDirectory(8);
		setDirectory(9);
		setDirectory(10);
		$('.hFinderDirectory1').mousedown(function() {$('.hFinderDirectory1').css('background-color','lightblue')});
		$('.hFinderDirectory2').mousedown(function() {$('.hFinderDirectory2').css('background-color','lightblue')});
		$('.hFinderDirectory3').mousedown(function() {$('.hFinderDirectory3').css('background-color','lightblue')});
		$('.hFinderDirectory4').mousedown(function() {$('.hFinderDirectory4').css('background-color','lightblue')});
		$('.hFinderDirectory5').mousedown(function() {$('.hFinderDirectory5').css('bahkground-color','lightblue')});
		$('.hFinderDirectory6').mousedown(function() {$('.hFinderDirectory6').css('background-color','lightblue')});
		$('.hFinderDirectory7').mousedown(function() {$('.hFinderDirectory7').css('background-color','lightblue')});
		$('.hFinderDirectory8').mousedown(function() {$('.hFinderDirectory8').css('background-color','lightblue')});
		$('.hFinderDirectory9').mousedown(function() {$('.hFinderDirectory9').css('background-color','lightblue')});
		$('.hFinderDirectory10').mousedown(function() {$('.hFinderDirectory10').css('background-color','lightblue')});
	}
);
