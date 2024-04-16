from flask import Flask, render_template, request, flash, redirect
from flask_caching import Cache # Importing Flask-Caching extension


app = Flask(__name__)
app.secret_key = 'ppcalapp'

# Adding caching configuration
app.config['CACHE_TYPE'] = 'null'
cache = Cache(app)

@app.route("/PPCalculator")
def index():
    return render_template("index.html")

@app.route("/calculate_pp", methods=["POST", "GET"])
def calculate_pp():
    try:
        session_total = int(request.form['session_total'])
        sessions_covered = int(request.form['sessions_covered'])
        salary_tier = request.form['salary_tier']

        if salary_tier == "CoachX":
            if session_total < 34:
                salary = 47.00
            elif 35 <= session_total <= 39:
                salary = 50.83
            elif 40 <= session_total <= 44:
                salary = 58.42
            elif 45 <= session_total <= 54:
                salary = 62.42
            elif 55 <= session_total <= 64:
                salary = 65.42
            else:
                salary = 68.42
        elif salary_tier == "Coach":
            if session_total < 34:
                salary = 27.67
            elif 35 <= session_total <= 39:
                salary = 31.59
            elif 40 <= session_total <= 44:
                salary = 43.08
            elif 45 <= session_total <= 54:
                salary = 46.08
            elif 55 <= session_total <= 64:
                salary = 49.16
            else:
                salary = 51.66
        elif salary_tier == "Coach+":
            if session_total < 34:
                salary = 33.67
            elif 35 <= session_total <= 39:
                salary = 37.59
            elif 40 <= session_total <= 44:
                salary = 48.42
            elif 45 <= session_total <= 54:
                salary = 51.92
            elif 55 <= session_total <= 64:
                salary = 55.50
            else:
                salary = 58.50

        pay_period_salary = salary * session_total
        total_pay_period_salary_scenario_A = (sessions_covered * 7.00) + (session_total * salary)

        if sessions_covered > 0:
            session_total_b = session_total + sessions_covered
            if salary_tier == "CoachX":
                if session_total_b < 34:
                    salary_b = session_total * 47.00
                elif 35 <= session_total_b <= 39:
                    salary_b = session_total * 50.83
                elif 40 <= session_total_b <= 44:
                    salary_b = session_total * 58.42
                elif 45 <= session_total_b <= 54:
                    salary_b = session_total * 62.42
                elif 55 <= session_total_b <= 64:
                    salary_b = session_total * 65.42
                else:
                    salary_b = session_total * 68.42
            elif salary_tier == "Coach":
                if session_total_b < 34:
                    salary_b = session_total * 27.67
                elif 35 <= session_total_b <= 39:
                    salary_b = session_total * 31.59
                elif 40 <= session_total_b <= 44:
                    salary_b = session_total * 43.08
                elif 45 <= session_total_b <= 54:
                    salary_b = session_total * 46.08
                elif 55 <= session_total_b <= 64:
                    salary_b = session_total * 49.16
                else:
                    salary_b = session_total * 51.66
            elif salary_tier == "Coach+":
                if session_total_b < 34:
                    salary_b = session_total * 33.67
                elif 35 <= session_total_b <= 39:
                    salary_b = session_total * 37.59
                elif 40 <= session_total_b <= 44:
                    salary_b = session_total * 48.42
                elif 45 <= session_total_b <= 54:
                    salary_b = session_total * 51.92
                elif 55 <= session_total_b <= 64:
                    salary_b = session_total * 55.50
                else:
                    salary_b = session_total * 58.50

        if sessions_covered == 0:
            flash("Your salary is: £{:.2f}".format(pay_period_salary))
        else:
            flash("Scenario A(£7): Your salary is: £{:.2f}\nScenario B: Your salary is: £{:.2f}".format(total_pay_period_salary_scenario_A, salary_b))
    except ValueError:
        flash("Error: Please enter valid values for session total and sessions covered")

    return redirect("/PPCalculator")

if __name__ == '__main__':
    app.run(debug=True)