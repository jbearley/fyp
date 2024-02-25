document.addEventListener('DOMContentLoaded', () => {
	resizer();
});

/**
 * Give the vertical resize line functionality.
 */
function resizer() {
	const $resizer = document.querySelector('.your-information .resizer');
	if ($resizer) {
		const stopListening = () => {
			document.removeEventListener('mouseup', stopListening);
			document.removeEventListener('mousemove', resize);
			document.querySelectorAll('section').forEach($section => {
				$section.style.userSelect = 'initial';
			});
			document.querySelector('.your-information .resizer').style.filter = '';
		};
		const resize = (event) => {
			document.querySelector('.your-information').style.width = `${Math.max(224, Math.min(500, event.clientX))}px`;
		};
		const startListening = () => {
			document.addEventListener('mouseup', stopListening);
			document.addEventListener('mousemove', resize);
			document.querySelectorAll('section').forEach($section => {
				$section.style.userSelect = 'none';
			});
			document.querySelector('.your-information .resizer').style.filter = 'brightness(0.96)';
		};
		$resizer.addEventListener('mousedown', startListening);
	}
}