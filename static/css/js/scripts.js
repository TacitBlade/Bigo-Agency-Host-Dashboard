// Custom JavaScript for Bigo Agency Dashboard

document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading states to buttons
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
            }
        });
    });

    // Tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Chart period toggle functionality
    const periodButtons = document.querySelectorAll('[data-period]');
    periodButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            periodButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Here you would typically reload chart data
            console.log('Selected period:', this.getAttribute('data-period'));
        });
    });

    // Real-time data simulation (for demo purposes)
    function simulateRealTimeUpdates() {
        const statsCards = document.querySelectorAll('.card h4');
        
        setInterval(() => {
            statsCards.forEach(card => {
                const currentValue = parseInt(card.textContent.replace(/[^0-9]/g, ''));
                if (currentValue && Math.random() > 0.7) {
                    const change = Math.floor(Math.random() * 10) - 5; // Random change between -5 and +5
                    const newValue = Math.max(0, currentValue + change);
                    
                    if (card.textContent.includes('$')) {
                        card.textContent = '$' + newValue.toLocaleString();
                    } else {
                        card.textContent = newValue.toLocaleString();
                    }
                    
                    // Add a subtle animation
                    card.style.transform = 'scale(1.05)';
                    setTimeout(() => {
                        card.style.transform = 'scale(1)';
                    }, 200);
                }
            });
        }, 30000); // Update every 30 seconds
    }

    // Initialize real-time updates on dashboard page
    if (window.location.pathname === '/' || window.location.pathname.includes('dashboard')) {
        simulateRealTimeUpdates();
    }

    // Table sorting functionality
    const tables = document.querySelectorAll('.table');
    tables.forEach(table => {
        const headers = table.querySelectorAll('th');
        headers.forEach((header, index) => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', () => sortTable(table, index));
        });
    });

    function sortTable(table, column) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));
        
        rows.sort((a, b) => {
            const aValue = a.cells[column].textContent.trim();
            const bValue = b.cells[column].textContent.trim();
            
            // Check if values are numbers
            const aNum = parseFloat(aValue.replace(/[^0-9.-]/g, ''));
            const bNum = parseFloat(bValue.replace(/[^0-9.-]/g, ''));
            
            if (!isNaN(aNum) && !isNaN(bNum)) {
                return bNum - aNum; // Descending for numbers
            } else {
                return aValue.localeCompare(bValue); // Ascending for text
            }
        });
        
        // Re-append sorted rows
        rows.forEach(row => tbody.appendChild(row));
        
        // Add visual feedback
        const headers = table.querySelectorAll('th');
        headers.forEach(h => h.classList.remove('sorted'));
        headers[column].classList.add('sorted');
    }

    // Add CSS for sorted headers
    const style = document.createElement('style');
    style.textContent = `
        .table th.sorted {
            background-color: #e9ecef !important;
            position: relative;
        }
        .table th.sorted::after {
            content: '↓';
            position: absolute;
            right: 8px;
            color: #6c757d;
        }
    `;
    document.head.appendChild(style);

    // Form validation
    const validationForms = document.querySelectorAll('form');
    validationForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('input[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    field.classList.add('is-invalid');
                    isValid = false;
                } else {
                    field.classList.remove('is-invalid');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
});

// Utility functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function formatNumber(num) {
    return new Intl.NumberFormat('en-US').format(num);
}

// Export functions for use in other scripts
window.DashboardUtils = {
    formatCurrency,
    formatNumber
};