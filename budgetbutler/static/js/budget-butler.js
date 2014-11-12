var options = {
    modalTitle: 'Budget Butler'

};

(function (BudgetButler, $) {
    var expenseMonthView = BudgetButler.addView('.expenses-month-view', {
        dynamicNavbar: true
    });

    $('body').on('click', '.navbar-inner > .left', function () { expenseMonthView.back() });
})(new Framework7(options), Dom7);