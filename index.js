 // Select all buttons with name "action"
document.querySelectorAll('button[name="action"]').forEach(button => {
    button.addEventListener('click', function() {
        // Get the parent form element
        const form = this.closest('form');
        // Remove 'active' class from all buttons inside the form
        form.querySelectorAll('button[name="action"]').forEach(btn => {
            btn.classList.remove('active');
        });
        // Add 'active' class to the clicked button
        this.classList.add('active');
    });
});
 
