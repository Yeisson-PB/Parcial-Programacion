from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def dashboard():
    return render_template('index.html')

#Component
@app.route('/components-alerts.html')
def components_alerts():
    return render_template('components-alerts.html')

@app.route('/components-accordion.html')
def components_accordion():
    return render_template('components-accordion.html')

@app.route('/components-badges.html')
def components_badges():
    return render_template('components-badges.html')

@app.route('/components-breadcrumbs.html')
def components_breadcrumbs():
    return render_template('components-breadcrumbs.html')

@app.route('/components-buttons.html')
def components_buttons():
    return render_template('components-buttons.html')

@app.route('/components-cards.html')
def components_cards():
    return render_template('components-cards.html')

@app.route('/components-carousel.html')
def components_carousel():
    return render_template('components-carousel.html')

@app.route('/components-list-group.html')
def components_list_group():
    return render_template('components-list-group.html')

@app.route('/components-modal.html')
def components_modal():
    return render_template('components-modal.html')

@app.route('/components-tabs.html')
def components_tabs():
    return render_template('components-tabs.html')

@app.route('/components-pagination.html')
def components_pagination():
    return render_template('components-pagination.html')

@app.route('/components-progress.html')
def components_progress():
    return render_template('components-progress.html')

@app.route('/components-spinners.html')
def components_spinners():
    return render_template('components-spinners.html')

@app.route('/components-tooltips.html')
def components_tooltips():
    return render_template('components-tooltips.html')

#Forms
@app.route('/forms-elements.html')
def forms_elements():
    return render_template('forms-elements.html')

@app.route('/forms-layouts.html')
def forms_layouts():
    return render_template('forms-layouts.html')

@app.route('/forms-editors.html')
def forms_editors():
    return render_template('forms-editors.html')

@app.route('/forms-validation.html')
def forms_validation():
    return render_template('forms-validation.html')

#tables
@app.route('/tables-general.html')
def tables_general():
    return render_template('tables-general.html')

@app.route('/tables-data.html')
def tables_data():
    return render_template('tables-data.html')

#Charts
@app.route('/charts-chartjs.html')
def charts_chartjs():
    return render_template('charts-chartjs.html')

@app.route('/charts-apexcharts.html')
def charts_apexcharts():
    return render_template('charts-apexcharts.html')

@app.route('/charts-echarts.html')
def charts_echarts():
    return render_template('charts-echarts.html')

#Icons
@app.route('/icons-bootstrap.html')
def icons_bootstrap():
    return render_template('icons-bootstrap.html')

@app.route('/icons-remix.html')
def icons_remix():
    return render_template('icons-remix.html')

@app.route('/icons-boxicons.html')
def icons_boxicons():
    return render_template('icons-boxicons.html')

#Demas
@app.route('/users-profile.html')
def users_profile():
    return render_template('users-profile.html')

@app.route('/pages-faq.html')
def pages_faq():
    return render_template('pages-faq.html')

@app.route('/pages-contact.html')
def pages_contact():
    return render_template('pages-contact.html')

@app.route('/pages-register.html')
def pages_register():
    return render_template('pages-register.html')

@app.route('/pages-login.html')
def pages_login():
    return render_template('pages-login.html')

@app.route('/pages-error-404.html')
def pages_error_404():
    return render_template('pages-error-404.html')

@app.route('/pages-blank.html')
def pages_blank():
    return render_template('pages-blank.html')


if __name__ == '__main__':
    app.run(debug=True)