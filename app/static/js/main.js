document.addEventListener('DOMContentLoaded', () => {
	resizer();
	seeMore();
	expandCollapseAll();
	dropdowns();
	// inputSubmit();
	// inputSubmit3();
    inputSubmit2();
	requirementsChecklist();
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
		$dropdown.closest('.dropdown-container').querySelector('[class^="delete-"]').addEventListener('click', (e) => {
			const $toBeDeleted = e.currentTarget.closest('.dropdown-container');
			let $nextSibling = $toBeDeleted.nextElementSibling;
			while ($nextSibling && $nextSibling.classList.contains('dropdown-container')) {
				const $label = $nextSibling.querySelector('.label');
				$label.innerHTML = $label.innerHTML.replace(/(Major )(\d+)(.*)/, (match, p1, p2, p3) => {
					return p1 + (parseInt(p2) - 1) + p3;
				});
				$nextSibling = $nextSibling.nextElementSibling;
			}
			$toBeDeleted.remove();
		});

	};
	
	document.querySelectorAll('.dropdown').forEach($dropdown => {
		initializeDropdown($dropdown);
	});
	document.querySelectorAll('#add-major, #add-minor').forEach($btn => {
		$btn.addEventListener('click', (e) => {
			const category = e.currentTarget.id === 'add-major' ? 'major' : 'minor';
			e.preventDefault();
			let formOptions = '';
			let displayOptions = '';
			const options = e.currentTarget.getAttribute(`data-${category}s`).split(',');
			options.forEach(option => {
				formOptions += `<option value='${option}'>${option}</option>`;
				displayOptions += `<button class='option' value='${option}'>${option}</button>`;
			});
			const $dropdownContainer = document.createElement('div');
			$dropdownContainer.className = 'dropdown-container';
			const categoryTitleCase = category.charAt(0).toUpperCase() + category.substring(1);
			$dropdownContainer.innerHTML = `
			<button class='delete-${category}'></button>
			<select name='${category}s'>
				${formOptions}
			</select>
			<div class='dropdown'>
				<div class='label'>${categoryTitleCase}: <b>Select option...</b></div>
				<div class='options'>
					${displayOptions}
				</div>
			</div>
		`;
			initializeDropdown($dropdownContainer.querySelector('.dropdown'));
			e.currentTarget.insertAdjacentElement('beforebegin', $dropdownContainer);
		});
	});

	document.querySelector('#add-semester').addEventListener('click', (e) => {
		e.preventDefault();
		let formOptions = '';
		let displayOptions = '';
		const semesters = e.currentTarget.getAttribute('data-semesters').split(',');
		semesters.forEach(semester => {
			formOptions += `<option value='${semester}'>${semester}</option>`;
			displayOptions += `<button class='option' value='${semester}'>${semester}</button>`;
		});
		const $dropdownContainer = document.createElement('div');
		$dropdownContainer.className = 'dropdown-container';
		$dropdownContainer.innerHTML = `
			<select name='semesters'>
				${formOptions}
			</select>
			<div class='dropdown'>
				<div class='label'>Semester: <b>Select option...</b></div>
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
    const formData = new FormData(form);
    let url = "majors=" + Array.from(formData.values()).join(",");
	return url;
}

function inputSubmit3() {
	const form = document.querySelector('#semesterselect');
    const formData = new FormData(form);
    let url = "semesters=" + Array.from(formData.values()).join(",");
	return url;
}

function inputSubmit2() {
	const $submitButton = document.querySelector("#submit-user-info");
	$submitButton.addEventListener("click", function (e) {
		e.preventDefault(); // Prevent default form submission behavior
		const formData = new FormData(document.querySelector('#minorselect'));
		const minors = "?minors=" + Array.from(formData.values()).join(",");
		var majors = inputSubmit();
		var semester = inputSubmit3();
		let url = minors + "&" + majors + "&" + semester;
		window.location.href = url;
	});
}

function requirementsChecklist() {
	const requirementsJSON = JSON.parse(document.querySelector('#requirements-overview').getAttribute('data-requirements'));
	const fypJSON = JSON.parse(document.querySelector('#by-semester').getAttribute('data-fyp'));
	let allClasses = [];
	Object.values(fypJSON).forEach(classes => {
		allClasses = [...allClasses, ...Object.keys(classes)];
	});
	const checked = [];
	const checkRequirements = (categoryKey, requirements) => {
		if (categoryKey === 'total_credits') { // credit requirement
			const requiredCredits = parseInt(requirements);
			const $checkbox = document.querySelector('[id="total_credits"]');
			let totalCredits = 0;
			document.querySelectorAll('.total-credits span').forEach($semesterCredits => {
				totalCredits += parseInt($semesterCredits.innerHTML);
			});
			const $label = $checkbox.nextElementSibling;
			$label.querySelector('.credits-met').innerHTML = totalCredits;
			if (totalCredits >= requiredCredits) {
				$checkbox.checked = true;
			}
			return;
		}
		Object.entries(requirements).forEach(([reqKey, classes]) => { // any requirement that is a mapping of 'requirementKey' => classes[]
			if (reqKey == 'singles') { // if the key is 'singles', every class in the list is required
				classes.forEach(classKey => {
					try {
						const $checkbox = document.querySelector(`[category-key="${categoryKey}"] [id="${reqKey}_${classKey}"]`);
						$checkbox.checked = true;
						checked.push(classKey);
					} catch {}
				});
				return;
			}
			// from here, reqKey should be in the form 'pick_<n>_<requirement label>'
			const [, numChoices, req] = reqKey.match(/pick_(\d+)_?(.*)/);
			let found = 0;
			let i = 0;
			while (i < classes.length) {
				if (allClasses.includes(classes[i])) {
					console.log('found ' + classes[i] + ' for ' + req);
					found++;
					checked.push(classes[i]);
					try {
						const $radioInput = document.querySelector(`[category-key="${categoryKey}"] [id="${reqKey}_${classes[i]}"]`);
						$radioInput.checked = true;
						$radioInput.closest('.choice-group').insertAdjacentElement('afterbegin', $radioInput.closest('label')); // move checked item to the top
					} catch { }
				}
				i++;
			}
			try {
				const $checkbox = document.querySelector(`[category-key="${categoryKey}"] [id="${req}"]`);
				if (found >= numChoices) {
					$checkbox.checked = true;
					found = numChoices;
				}
				const $label = $checkbox.nextElementSibling;
				$label.querySelector('.num-picked').innerHTML = found;
			} catch { }
		});
	};
	Object.entries(requirementsJSON).forEach(([key, value]) => {
		checkRequirements(key, value);
	});
}