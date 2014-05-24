$(document).ready(
	function() {
		var containmentTop = $("#hFinderFiles").position().top
		var containmentBottom = containmentTop + 1000
		$('.hFinderDirectory1').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory2').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory3').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory4').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory5').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory6').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory7').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory8').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory9').draggable({containment : [0,containmentTop,1000,containmentBottom]});
		$('.hFinderDirectory10').draggable({containment : [0,containmentTop,1000,containmentBottom]});
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
		$('.hFinderDrop').droppable({drop: function(event,ui) {alert(ui);}})
	}
);
function containerDiagnostic(theId,theFlyoutId,theFetchURL)
{
	var theUrl = theId;
	theUrl = theUrl + "/showContainerDiagnostics";
	alert(theUrl);
	alert(theFlyoutId);
        alert(theFetchURL);
	var theFlyout = $('#'+theFlyoutId);
	$.ajax({url: theFetchURL,
		flyout : theFlyout,
		success: function(data) {
			this.flyout.append(data);		
			this.flyout.css('position','absolute');
			this.flyout.css('left','100px');
			this.flyout.css('top','100px');
			this.flyout.css('background-color','yellow');
		}
	});
	//theBox = $('#'+theId);
	//theBox.css('background-color','#00FFFF');
	//height = theBox.css('height');
	//alert(height);
}
