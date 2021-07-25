function legalTerms() {

	var totalLegalRules = $('.legal__rule').length;

	if ( $('.legal').hasClass('is-expanded') ) {
		$('.legal__rules').attr('aria-expanded', 'true').attr('aria-hidden', 'false').css('opacity', '1.0').show();
		$('.legal__terms').on('scroll', function() {
			legalProgress();
		});
	}
	else {
		$('.legal__terms').on('scroll', function() {
			if($(this).scrollTop() + $(this).innerHeight() >= this.scrollHeight) {
				$('.legal__rules')
					.attr('aria-expanded', 'true')
					.attr('aria-hidden', 'false')
					.slideDown(100 * totalLegalRules + 10)
					.animate({opacity: "1"},175);
			}

			legalProgress();

		});
	}

}



function legalRules(){

	// Terms & Conditions - Checkbox
	$('.toggle--checkbox .toggle__label, .toggle--checkbox .toggle__disagree').remove();

	// Terms & Conditions - Buttons
	$('.toggle--buttons .control-indicator').remove();

	$(document).on('click', '.toggle--buttons .toggle__agree .checkbox', function(){

		if ( $(this).prop('checked', true) ) {
			$(this).parent('.toggle__agree').siblings('.toggle__disagree').find('.checkbox').prop('checked', false);

			// Terms & Conditions - Required Buttons
			$(this).closest('.legal__rule').css('background','#fff');

		}

	});

	$(document).on('click', '.toggle--buttons .toggle__disagree .checkbox', function(){

		if ( $(this).prop('checked', true) ) {
			$(this).parent('.toggle__disagree').siblings('.toggle__agree').find('.checkbox').prop('checked', false);

			// Terms & Conditions - Required Buttons
			if ( $(this).closest('.legal__rule').hasClass('is-required') ) {
				$(this).closest('.legal__rule').css('background','#fdf6f6');
			}

		}

	});

}



function legalProgress() {
	var legalTermsScrollHeight = $('.legal__terms-scroll').height() - $('.legal__terms').height();
	var legalTermsScrollTop = $('.legal__terms').scrollTop();
	var legalProgress = Math.max(0, Math.min(1, legalTermsScrollTop / legalTermsScrollHeight));
	$('.legal__progress').css({width : legalProgress * 100 + '%' + 10 + 'px'});
}



function overlay(){

	$(document).on('click', '.overlay--open', function() {
		$('body').css('overflow','hidden');
		$('.overlay').fadeIn(200);
		$('.overlay > .container').fadeIn(400).animate({marginTop : "10px"}, 800);
	});

	$(document).on('click', '.overlay--close', function() {
		$('body').css('overflow','visible');
		$('.overlay > .container').fadeOut(400).animate({marginTop : "10px"}, 800);
		$('.overlay').fadeOut(200);
	});

}

overlay();
legalTerms(); 
legalRules();