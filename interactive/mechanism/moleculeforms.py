from django import forms
from .mech_load import initialize_form

class MoleculeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MoleculeForm, self).__init__(*args, **kwargs)
        inits = initialize_form()

        self.fields['formula'] = forms.CharField(initial=inits['formula'],required=False)
        self.fields['solve'] = forms.CharField(initial=inits['solve'])
        self.fields['transport'] = forms.CharField(initial=inits['transport'])
        self.fields['hl.henrys_law_type'] = forms.IntegerField(initial=inits['henrys_law']['henrys_law_type'])
        self.fields['hl.kh_298'] = forms.FloatField(initial=inits['henrys_law']['kh_298'])
        self.fields['hl.dh_r'] = forms.FloatField(initial=inits['henrys_law']['dh_r'])
        self.fields['hl.k1_298'] = forms.FloatField(initial=inits['henrys_law']['k1_298'])
        self.fields['hl.dh1_r'] = forms.FloatField(initial=inits['henrys_law']['dh1_r'])
        self.fields['hl.k2_298'] = forms.FloatField(initial=inits['henrys_law']['k2_298'])
        self.fields['hl.dh2_r'] = forms.FloatField(initial=inits['henrys_law']['dh2_r'])
        self.fields['molecular_weight'] = forms.FloatField(initial=inits['molecular_weight'])
        self.fields['standard_name'] = forms.CharField(initial=inits['standard_name'])
    

class NewMoleculeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(NewMoleculeForm, self).__init__(*args, **kwargs)
        
        self.fields['moleculename'] = forms.CharField()
        self.fields['formula'] = forms.CharField()
        self.fields['solve'] = forms.CharField()
        self.fields['transport'] = forms.CharField()
        self.fields['hl.henrys_law_type'] = forms.IntegerField()
        self.fields['hl.kh_298'] = forms.FloatField()
        self.fields['hl.dh_r'] = forms.FloatField()
        self.fields['hl.k1_298'] = forms.FloatField()
        self.fields['hl.dh1_r'] = forms.FloatField()
        self.fields['hl.k2_298'] = forms.FloatField()
        self.fields['hl.dh2_r'] = forms.FloatField()
        self.fields['molecular_weight'] = forms.FloatField()
        self.fields['standard_name'] = forms.CharField()


class MoleculeSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MoleculeSearchForm, self).__init__(*args, **kwargs)
        self.fields['query'] = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'name'}))