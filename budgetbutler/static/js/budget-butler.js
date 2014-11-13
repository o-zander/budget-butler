var options = {
    modalTitle: 'Budget Butler'

};

(function (BudgetButler, $) {
    var body = $('body'),
        addExpensePopUp = $('.add-expense-popup'),
        addExpensePopUpUrl = addExpensePopUp.data('url'),
        addExpensePopUpContent = addExpensePopUp.find('.add-expense-popup-content'),

        expenseMonthView = BudgetButler.addView('.expenses-month-view', {
        dynamicNavbar: true
    });

    body.on('click', '.navbar-inner > .left', function () { expenseMonthView.back() });

    addExpensePopUp
        .on('open', function () {
            addExpensePopUpContent.load(addExpensePopUpUrl);
        })
        .on('click', '.form-submit', function (e) {
            e.preventDefault();
            var form = addExpensePopUp.find('form'), url = form.attr('action');
            $.post(url, form.serialize(), function (data, status, jqXHR) {
                if (jqXHR.status == 201) {
                    expenseMonthView.router.refreshPage();
                    BudgetButler.closeModal('.add-expense-popup');
                } else {
                    addExpensePopUpContent.empty().append(data);
                }
            });
        });
})(new Framework7(options), jQuery);