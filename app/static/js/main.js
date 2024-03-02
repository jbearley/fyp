document.addEventListener('DOMContentLoaded', () => {
	resizer();
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