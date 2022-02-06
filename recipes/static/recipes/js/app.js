// function debounce(func, wait = 20, immediate = true) {
// 	var timeout;
// 	return function() {
// 	  var context = this, args = arguments;
// 	  var later = function() {
// 		timeout = null;
// 		if (!immediate) func.apply(context, args);
// 	  };
// 	  var callNow = immediate && !timeout;
// 	  clearTimeout(timeout);
// 	  timeout = setTimeout(later, wait);
// 	  if (callNow) func.apply(context, args);
// 	};
// };

// const sliderImages = document.querySelectorAll('.slide-in', );
// function checkSlide(e) {
//   sliderImages.forEach(sliderImage => {
// 	//halfway through image
// 	const slideInAt = (window.scrollY + window.innerHeight) - sliderImage.height / 2;
// 	//bottom of image
// 	const imageBottom = sliderImage.offsetTop + sliderImage.height;
// 	const isHalfShown = slideInAt > sliderImage.offsetTop;
// 	const isNotScrolledPast = window.scrollY < imageBottom;
// 	if(isHalfShown && isNotScrolledPast) {
// 	  sliderImage.classList.add('active');
// 	} else {
// 	  sliderImage.classList.remove('active');

// 	}
//   });
// }

// window.addEventListener('scroll', debounce(checkSlide));

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

