document.addEventListener('DOMContentLoaded', () => {
	dropdowns();
	inputSubmit2();
	if (!document.querySelector('#your-information').classList.contains('initial')) {
		resizer();
		seeMore();
		expandCollapseAll();
		requirementsChecklist();
	}
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

/* Dynamically add see-more functionality to the class containers in the fyp panel; also adds see-more functionality to checklist item with choices */
function seeMore() {
	if (document.querySelector('#your-information').classList.contains('initial')) return; // in the initial view, we don't have any see-more stuff to deal with
	const expandListener = (event) => { // event function for toggling 'expanded' class on click
		if (event.currentTarget.classList.contains('expanded')) {
			event.currentTarget.classList.remove('expanded');
		} else {
			event.currentTarget.classList.add('expanded');
		}
	};
	const updateSeeMoreStatus = ($classContainer) => { // checks given element for overflow and adds/removes class 'see-more-container'
		if ($classContainer.scrollWidth > $classContainer.clientWidth + 4) {
			$classContainer.classList.add('see-more-container');
			$classContainer.addEventListener('click', expandListener);
		} else {
			$classContainer.classList.remove('see-more-container');
			$classContainer.removeEventListener('click', expandListener);
		}
	};
	let prevWidth = document.querySelector('#by-semester').clientWidth;
	const resizeObserver = new ResizeObserver(entries => {
		for (const entry of entries) {
			if (document.querySelector('#by-semester').clientWidth === prevWidth) return;
			console.log('resized');
			document.querySelectorAll('.class-container').forEach($classContainer => {
				updateSeeMoreStatus($classContainer);
			});
		}
	});
	/* give class 'see-more-container' to classes with overflow text in the fyp */
	document.querySelectorAll('.class-container').forEach($classContainer => {
		updateSeeMoreStatus($classContainer);
	});
	resizeObserver.observe(document.querySelector('#by-semester'));
	/* add event listener to all elements of class 'see-more-container' */
	document.querySelectorAll('.see-more-container').forEach($classContainer => {
		$classContainer.addEventListener('click', expandListener);
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
			<select name='${category}s' value=''>
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
	console.log(requirementsJSON);
	console.log(fypJSON);
	let allClasses = []; // all classes in the fyp
	Object.values(fypJSON).forEach(classesObj => { // add all classes from the fyp to allClasses
		Object.values(classesObj).forEach(classObj => {
			allClasses.push(classObj.title);
		});
	});
	const checked = []; // list that should contain electives selected by either the fyp algorithm or the user
	const incompleteReqs = [];
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
				$label.classList.add('completed');
			} else {
				$label.classList.add('started');
				incompleteReqs.push(categoryKey);
			}
			return;
		}
		if (categoryKey === 'AOIs') { // temporary AOI stuff !!!!!not legit
			document.querySelectorAll(`[category-key="${categoryKey}"] input`).forEach($checkbox => {
				$checkbox.checked = true;
				const $label = $checkbox.nextElementSibling;
				$label.classList.add('completed');
				$label.querySelector('.num-picked').innerHTML = $label.querySelector('.num-choices').innerHTML;
			});
			return;
		}
		Object.entries(requirements).forEach(([reqKey, classes]) => { // each requirement is a mapping of 'requirementKey' => classes[]
			if (reqKey == 'singles') { // if the key is 'singles', every class in the list is required
				classes.forEach(classKey => {
					if (allClasses.includes(classKey)) {
						try {
							const $checkbox = document.querySelector(`[category-key="${categoryKey}"] [id="${reqKey}_${classKey}"]`);
							$checkbox.checked = true;
							checked.push(classKey);
							const $label = $checkbox.nextElementSibling;
							$label.classList.add('completed');
						} catch { }
					} else {
						incompleteReqs.push(classKey);
						try {
							const $checkbox = document.querySelector(`[category-key="${categoryKey}"] [id="${reqKey}_${classKey}"]`);
							const $label = $checkbox.nextElementSibling;
							$label.classList.add('notStarted');
						} catch { }
					}
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
				let progress = 'started';
				if (found >= numChoices) {
					$checkbox.checked = true;
					found = numChoices;
					progress = 'completed';
				} else if (found == 0) {
					progress = 'notStarted';
				}
				if (progress !== 'completed') {
					incompleteReqs.push(req);
					/* move item to the top */
					const $choiceGroup = $checkbox.closest('.choice-group');
					$choiceGroup.closest('.reqs').insertAdjacentElement('afterbegin', $choiceGroup);
				}
				/* style label */
				const $label = $checkbox.nextElementSibling;
				$label.querySelector('.num-picked').innerHTML = found;
				$label.classList.add(progress);
			} catch { }
		});
	};
	Object.entries(requirementsJSON).forEach(([key, value]) => {
		checkRequirements(key, value);
	});
	if (incompleteReqs.length) {
		const $section = document.querySelector('#requirements-overview');
		$section.classList.add('incomplete');
		const noticeHTML = `<div class='notice tooltip-container'>
			<div class='icon'></div>
			<div class='tooltip'>
			
			</div>
		</div>`
		$section.querySelector('header h1').insertAdjacentHTML('beforeend', noticeHTML);
	}
	
}