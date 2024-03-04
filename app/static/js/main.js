document.addEventListener('DOMContentLoaded', () => {
	resizer();
	seeMore();
	inputFields();
});

/**
 * Give the vertical resize line functionality.
 */
function resizer() {
	document.querySelectorAll('.resizer').forEach($resizer => {
		const sectionSelector = `#${$resizer.closest('section').id}`;
		const stopListening = () => {
			document.removeEventListener('mouseup', stopListening);
			document.removeEventListener('mousemove', resize);
			document.querySelectorAll('section').forEach($section => {
				$section.style.userSelect = 'initial';
			});
			document.querySelector(`${sectionSelector} .resizer`).style.filter = '';
		};
		const resize = (event) => {
			const sectionLeft = document.querySelector(sectionSelector).getBoundingClientRect().left;
			document.querySelector(sectionSelector).style.width = `${Math.max(240, Math.min(500, event.clientX - sectionLeft))}px`;
		};
		const startListening = () => {
			document.addEventListener('mouseup', stopListening);
			document.addEventListener('mousemove', resize);
			document.querySelectorAll('section').forEach($section => {
				$section.style.userSelect = 'none';
			});
			document.querySelector(`${sectionSelector} .resizer`).style.filter = 'brightness(0.96)';
		};
		$resizer.addEventListener('mousedown', startListening);
	});
}

function seeMore() {
	document.querySelectorAll('.class-container').forEach($classContainer => {
		$classContainer.addEventListener('click', (event) => {
			if (event.currentTarget.classList.contains('expanded')) {
				event.currentTarget.classList.remove('expanded');
			} else {
				event.currentTarget.classList.add('expanded');
			}
		});
	});
}

/**
 * Add event listeners to dropdowns.
 */
function inputFields() {
	document.querySelectorAll('.dropdown button').forEach($dropdownButton => {
		$dropdownButton.addEventListener('click', function (event) {
			if (event.currentTarget.classList.contains("expanded")) {
				event.currentTarget.classList.remove("expanded");
			} else {
				event.currentTarget.classList.add("expanded");
			}
		});
	});
}

function toggleImages(button) {

	var image1 = button.querySelector('.image1');
	var image2 = button.querySelector('.image2');

	if (image1.style.display === 'none' || image1.style.display === '') {
		image1.style.display = 'block'; // Display the first image
		image2.style.display = 'none';  // Hide the second image
	} else {
		image1.style.display = 'none';  // Hide the first image
		image2.style.display = 'block'; // Display the second image
	}
}