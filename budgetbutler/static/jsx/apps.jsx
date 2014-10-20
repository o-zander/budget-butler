/** @jsx React.DOM */

Date.prototype.toInputValue = function () {
    var zerofill = function (number) { return number < 10 ? '0' + number : number},
        year = this.getFullYear(), month = this.getMonth() + 1, date = this.getDate();
    return [year, zerofill(month), zerofill(date)].join('-');
};

(function ($, R) {
    var Arrow = R.createClass({
        getDirection: function () {
            return this.props.direction || 'left';
        },

        handleClick: function (event) {
            if (typeof this.props.onClick == 'function') this.props.onClick(event, this.getDirection());
        },

        render: function () {
            var className = ['glyphicon', 'arrow', 'glyphicon-chevron-' + this.getDirection()].join(' ');
            return (
                <button className='btn btn-default' onClick={this.handleClick}>
                    <span className={className} />
                </button>
            );
        }
    });

    var DatePicker = R.createClass({
        day: 60 * 60 * 24 * 1000,

        handleArrowClick: function (event, direction) {
            this.props.onDateChange(
                direction == 'left' ?
                    new Date(+this.props.date - this.day) :
                    new Date(+this.props.date + this.day)
            );
        },

        handleInputChange: function (event) {
            this.props.onDateChange(event.target.valueAsDate);
        },

        render: function () {
            return (
                <div className='row date-picker'>
                    <div className='col-xs-3'>
                        <Arrow direction='left' onClick={this.handleArrowClick} />
                    </div>
                    <div className='col-xs-6'>
                        <input className='form-control' type='date' value={this.props.date.toInputValue()} onChange={this.handleInputChange} />
                    </div>
                    <div className='col-xs-3'>
                        <Arrow direction='right' onClick={this.handleArrowClick} />
                    </div>
                </div>
            );
        }
    });

    var Expense = R.createClass({
        render: function () {
            return (
                <tr className='expense'>
                    <td>{this.props.data.description}</td>
                    <td>{this.props.data.amount}</td>
                </tr>
            );
        }
    });

    var ExpenseList = R.createClass({
        render: function () {
            var sum = 0,
                expenses = this.props.expenses.map(function (expense) {
                    sum += expense.amount;
                    return <Expense data={expense} />;
                });

            return (
                <table className='table expense-list'>
                    <thead>
                        <tr>
                            <th>Description</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        {expenses}
                        <tr className='expense-sum'>
                            <td>Sum:</td>
                            <td>{sum}</td>
                        </tr>
                    </tbody>
                </table>
            );
        }
    });

    var ExpenseView = R.createClass({
        getInitialState: function () {
            return {'date': new Date(), 'expenses': []}
        },

        componentDidMount: function () {
            $.ajax({
                url: this.getUrl(),
                dataType: 'json',
                success: function (data) {
                    this.setState(data);
                }.bind(this),
                error: function (xhr, status, err) {
                    console.error(this.props.url, status, err.toString());
                }.bind(this)
            });
        },

        getUrl: function () {
            return $('html').data('expenses-url');
        },

        handleDateChange: function (date) {
            this.setState({'date': date});
        },

        render: function () {
            var date = this.state.date, dateInputValue = date.toInputValue(),
                expenses = this.state.expenses.filter(function (expense) { return expense.date == dateInputValue });

            return (
                <div className='expense-view'>
                    <DatePicker date={date} onDateChange={this.handleDateChange} />
                    <ExpenseList expenses={expenses} />
                </div>
            );
        }
    });

    $(function () {
        R.renderComponent(
            <ExpenseView />,
            $('#content').get(0)
        );
    });
})(jQuery, React);