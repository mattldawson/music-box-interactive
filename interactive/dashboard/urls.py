from django.urls import path, include

from . import views 

app_name = 'dashboard'
urlpatterns = [
    path('',          views.landing_page, name='default'),
    path('home',          views.landing_page, name='default'),
    path('getting_started', views.getting_started_page, name='getting started'),
    path('visualize', views.visualize, name='visualize'),
    path('conditions', views.options),
    path('conditions/options', views.options, name='options'),
    path('conditions/initial', views.initial_conditions, name='inital conditions'),
    path('conditions/evolving', views.evolving_conditions, name='evolving conditions'),
    path('conditions/initial-species-concentrations', views.initial_species_concentrations_handler),
    path('conditions/initial-species-concentrations-save', views.initial_species_concentrations_save_handler),
    path('conditions/initial-reaction-rates', views.initial_reaction_rates_handler),
    path('conditions/initial-reaction-rates-save', views.initial_reaction_rates_save_handler),
    path('conditions/cond-csv', views.init_csv),
    path('conditions/evolving-file', views.evolv_file),
    path('conditions/download_config', views.download_file),
    path('conditions/config_json', views.config_json),
    path('conditions/linear_combination_form', views.linear_combination_form),
    path('conditions/evolv-linear-combo', views.evolv_linear_combo),
    path('conditions/evolving-linear-combination', views.evolving_linear_combination),
    path('conditions/logging-toggle', views.toggle_logging),
    path('conditions/logging-toggle-check', views.toggle_logging_check),
    path('conditions/clear-evolv-files', views.clear_evolv_files),
    path('conditions/load-example', views.load_example),
    path('conditions/examplefile', views.example_file),
    path('conditions/remove-linear-combination', views.remove_linear),
    path('conditions/report', views.report_bug),
    path('download_config', views.download_file),
    path('download', views.download_handler, name='download')
]
