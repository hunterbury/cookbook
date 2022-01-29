function debounce(func, wait = 20, immediate = true) {
	var timeout;
	return function() {
	  var context = this, args = arguments;
	  var later = function() {
		timeout = null;
		if (!immediate) func.apply(context, args);
	  };
	  var callNow = immediate && !timeout;
	  clearTimeout(timeout);
	  timeout = setTimeout(later, wait);
	  if (callNow) func.apply(context, args);
	};
};

const sliderImages = document.querySelectorAll('.slide-in', );
function checkSlide(e) {
  sliderImages.forEach(sliderImage => {
	//halfway through image
	const slideInAt = (window.scrollY + window.innerHeight) - sliderImage.height / 2;
	//bottom of image
	const imageBottom = sliderImage.offsetTop + sliderImage.height;
	const isHalfShown = slideInAt > sliderImage.offsetTop;
	const isNotScrolledPast = window.scrollY < imageBottom;
	if(isHalfShown && isNotScrolledPast) {
	  sliderImage.classList.add('active');
	} else {
	  sliderImage.classList.remove('active');

	}
  });
}

window.addEventListener('scroll', debounce(checkSlide));

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// var	$parent = $("#main"),
// 		$aside = $("#aside"),
// 		$asideTarget = $aside.find(".aside--details"),
// 		$asideClose = $aside.find(".close"),
// 		$tilesParent = $(".tiles-a"),
// 		$tiles = $tilesParent.find("a"),
// 		slideClass = "show-detail";

// 		// tile click
// 		$tiles.on("click", function(e){
// 			e.preventDefault();
// 			e.stopPropagation();
// 			if(!$("html").hasClass(slideClass)){
// 				$tiles.removeClass("active");
// 				$(this).addClass("active");
// 				$(this).attr("aria-expanded","true");
// 				loadTileData($(this));
// 			}else{
// 				killAside();
// 				$(this).attr("aria-expanded","false");
// 			}
// 		});

// 		// kill aside
// 		$asideClose.on("click", function(e){
// 			e.preventDefault();
// 			killAside();
// 		});

// 		// load data to aside
// 		function loadTileData(target){
// 			var $this = $(target),
// 					itemHtml = $this.find(".details").html();
// 					$asideTarget.html(itemHtml);
// 					showAside();
// 		}

// 		// show/hide aside
// 		function showAside(){
// 			if(!$("html").hasClass(slideClass)){
// 				$("html").toggleClass(slideClass);
// 				$aside.attr("aria-hidden","false");
// 				focusCloseButton();
// 			}
// 		}
		
// 		// handle esc key
// 		window.addEventListener("keyup", function(e){

// 			// grab key pressed
// 			var code = (e.keyCode ? e.keyCode : e.which);
			
// 			// escape
// 			if(code === 27){
// 				killAside();
// 			}

// 		}, false);

// 		// kill aside
// 		function killAside(){
// 			if($("html").hasClass(slideClass)){
// 				$("html").removeClass(slideClass);
// 				sendFocusBack();
// 				$aside.attr("aria-hidden","true");
// 				$tiles.attr("aria-expanded","false");
// 			}
// 		}

// 		// send focus to close button
// 		function focusCloseButton(){
// 			$asideClose.focus();	
// 		}

// 		// send focus back to item that triggered event
// 		function sendFocusBack(){
// 			$(".active").focus();
// 		}

// 		// handle body click to close off-canvas
// 		$parent.on("click",function(e){
// 			if($("html").hasClass(slideClass)){
// 				killAside();
// 			}
// 		});


