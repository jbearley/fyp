document.addEventListener('DOMContentLoaded', () => {
	resizer();
	seeMore();
	expandCollapseAll();
	inputFields();
	inputSubmit();
});

/**
 * Give the vertical resize lines functionality.
 */
function resizer() {
	const getSectionWidth = (newWidth) => {
		return Math.max(72, Math.min(500, newWidth));
	};
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
			const newWidth = event.clientX - sectionLeft;
			document.querySelector(sectionSelector).style.width = `${getSectionWidth(newWidth)}px`;
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
	let previousWindowWidth = document.body.clientWidth;
	window.addEventListener('resize', () => {
		const sections = document.querySelectorAll('section');
		if (!sections.length) {
			return; // This should never happen but just in case, we avoid division by 0
		}
		const change = document.body.clientWidth - previousWindowWidth;
		const changePerSection = change / sections.length;
		document.querySelectorAll('section:not(:last-of-type)').forEach($section => {
			$section.style.width = `${getSectionWidth($section.clientWidth + changePerSection)}px`;
		});
		previousWindowWidth = document.body.clientWidth;
	});
}

function seeMore() {
	document.querySelectorAll('.see-more-container').forEach($classContainer => {
		$classContainer.addEventListener('click', (event) => {
			if (event.currentTarget.classList.contains('expanded')) {
				event.currentTarget.classList.remove('expanded');
			} else {
				event.currentTarget.classList.add('expanded');
			}
		});
	});
}

function expandCollapseAll() {
	document.querySelector('#expand-all').addEventListener('click', () => {
		document.querySelectorAll('.class-container').forEach($classContainer => {
			$classContainer.classList.add('expanded');
		});
	});
	document.querySelector('#collapse-all').addEventListener('click', () => {
		document.querySelectorAll('.class-container').forEach($classContainer => {
			$classContainer.classList.remove('expanded');
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

function inputSubmit() {
	const form = document.querySelector("#majorselect");
	form.addEventListener("submit", function (e) {
		e.preventDefault(); // Prevent default form submission behavior
		const $form = e.currentTarget;
		const formData = new FormData($form);
		let url = "?majors=";
		for (const value of formData.values()) {
			url += value + ",";
		}
		url = url.slice(0, -1); // Remove the trailing ','
		window.location.href = url;
	});
}