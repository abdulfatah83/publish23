document.addEventListener('DOMContentLoaded', () => {
    // UI Elements
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const errorMsg = document.getElementById('errorMsg');

    // Modal Elements
    const resultModal = document.getElementById('resultModal');
    const closeModalBtn = document.getElementById('closeModal');
    const printBtn = document.getElementById('printBtn');

    // Data Elements
    const studentNameEl = document.getElementById('studentName');
    const seatNumberEl = document.getElementById('seatNumber');
    const examHallEl = document.getElementById('examHall');
    const enrollmentNumberEl = document.getElementById('enrollmentNumber');
    const academicYearEl = document.getElementById('academicYear');

    // Load Data Check
    let studentData = [];
    if (window.studentData) {
        studentData = window.studentData;
        console.log('Data loaded from JS:', studentData.length, 'records');
    } else {
        console.error('Data not found. Make sure data.js is loaded.');
        errorMsg.textContent = 'خطأ: لم يتم تحميل قاعدة البيانات.';
    }

    // Search Function
    function performSearch() {
        const query = searchInput.value.trim();
        errorMsg.textContent = '';

        if (!query) {
            errorMsg.textContent = 'الرجاء إدخال رقم القيد';
            return;
        }

        // Search logic
        const student = studentData.find(s => String(s['رقم القيد']).trim() === query);

        if (student) {
            displayResult(student);
        } else {
            errorMsg.textContent = 'لم يتم العثور على طالب بهذا الرقم. يرجى التأكد من الرقم والمحاولة مرة أخرى.';
        }
    }

    // Display Result in Modal
    function displayResult(student) {
        studentNameEl.textContent = student['اسم الطالب'] || '--';
        seatNumberEl.textContent = student['رقم الجلوس'] || '--';
        enrollmentNumberEl.textContent = student['رقم القيد'] || '--';
        academicYearEl.textContent = student['السنة الدراسية'] || '--';

        const hall = student['القاعة الدراسية'];
        if (hall && String(hall).toLowerCase() !== 'nan' && String(hall).trim() !== '') {
            examHallEl.textContent = hall;
        } else {
            examHallEl.textContent = 'غير محدد';
        }

        // Show Modal
        resultModal.classList.add('active');
    }

    // Close Modal
    function closeModal() {
        resultModal.classList.remove('active');
    }

    // Print Function
    function printResult() {
        window.print();
    }

    // Event Listeners
    searchBtn.addEventListener('click', performSearch);

    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
        if (errorMsg.textContent) {
            errorMsg.textContent = '';
        }
    });

    closeModalBtn.addEventListener('click', closeModal);

    // Close modal if clicking outside content
    resultModal.addEventListener('click', (e) => {
        if (e.target === resultModal) {
            closeModal();
        }
    });

    printBtn.addEventListener('click', printResult);
});
