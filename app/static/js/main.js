document.addEventListener('DOMContentLoaded', () => {
	resizer();
	seeMore();
	expandCollapseAll();
	dropdowns();
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

function dropdowns() {
	const initializeDropdown = ($dropdown) => {
		/* click -> expand */
		$dropdown.addEventListener('click', (e) => {
			if (e.target.closest('.options')) {
				return;
			}
			const $dd = e.currentTarget;
			$dd.classList.toggle('expanded');
			if ($dd.classList.contains('expanded')) {
				/* set dropdown height */
				const height = window.innerHeight - $dd.getBoundingClientRect().bottom - 24;
				$dd.querySelector('.options').style.maxHeight = `${height}px`;
				const outsideClickListener = (e) => {
					if (!e.target.classList.contains('option') && e.target.closest('.dropdown') && e.target.closest('.dropdown').isEqualNode($dd)) return;
					$dd.classList.remove('expanded');
					document.removeEventListener('click', outsideClickListener);
				};
				document.addEventListener('click', outsideClickListener);
			}
		});

		/* click option -> set form value */
		$dropdown.querySelectorAll('.option').forEach($option => {
			$option.addEventListener('click', (e) => {
				e.preventDefault();
				e.target.closest('.dropdown-container').querySelector('select').value = e.currentTarget.value;
				e.target.closest('.dropdown').querySelector('.label b').innerHTML = e.currentTarget.innerHTML;
			});
		});

		/* delete */
		$dropdown.closest('.dropdown-container').querySelector('.delete-major').addEventListener('click', (e) => {
			// add code for delete
		});
	};
	document.querySelectorAll('.dropdown').forEach($dropdown => {
		initializeDropdown($dropdown);
	});
	document.querySelector('#add-major').addEventListener('click', (e) => {
		e.preventDefault();
		let formOptions = '';
		let majorNumber = document.querySelectorAll('.dropdown').length + 1;
		let displayOptions = '';
		const majors = e.currentTarget.getAttribute('data-majors').split(',');
		majors.forEach(major => {
			formOptions += `<option value='${major}'>${major}</option>`;
			displayOptions += `<button class='option' value='${major}'>${major}</button>`;
		});
		const $dropdownContainer = document.createElement('div');
		$dropdownContainer.className = 'dropdown-container';
		$dropdownContainer.innerHTML = `
			<button class='delete-major'></button>
			<select name='majors'>
				${formOptions}
			</select>
			<div class='dropdown'>
				<div class='label'>Major ${majorNumber}: <b>Select option...</b></div>
				<div class='options'>
					${displayOptions}
				</div>
			</div>
		`;
		initializeDropdown($dropdownContainer.querySelector('.dropdown'));
		e.currentTarget.insertAdjacentElement('beforebegin', $dropdownContainer);
	});
}

function inputSubmit() {
	const form = document.querySelector("#majorselect");
	form.addEventListener("submit", function (e) {
		e.preventDefault(); // Prevent default form submission behavior
		const formData = new FormData(e.currentTarget);
		formData.getAll('majors').forEach((value, i) => {
			console.log(value);
		});
		let url = "?majors=" + Array.from(formData.values()).join(",");
		window.location.href = url;
	});
}