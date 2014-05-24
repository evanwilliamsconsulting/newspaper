$(document).ready(function() {
	var putLeft=0;
	$('#contentActionMenus > li > dl').each(function(index,domEle)
	{
		var cAM = $("#contentActionMenus");
		var WW = $(window).width();
		var WH = $(window).height();
		cAMWidth = $(domEle).width();
		putLeft = WW - cAMWidth - 200;
		cAM.css('left',putLeft);
	}
	);
	$('#contentActionMenus > li > dl > dt > a >span').click(function(evt)
	{
		source = $(evt.target).parent();
		source2 = $(source).parent();
		source3 = $(source2).parent();
		dd = $(source3).children('dd');
		$(dd).toggle();
	});
	$('.pageone').each(function(index,domEle)
	{
		divid=$(domEle).attr('id');
		//alert(divid);
		select = "#" + divid + "> div";
		wrapbox = $(select);
		blockheight=wrapbox.height();
		//alert(wrapbox.width());
		richbox = $(wrapbox).find('.richcolumn');
	        richclass=$(richbox).attr('class');
		$(richbox).height(300);
		if (richclass=='richcolumn')
		{
			//alert('richcolumn');
	        	$(wrapbox).height(300);
			//alert(blockheight)
			//alert($(richbox).height());
		}
	});
});
