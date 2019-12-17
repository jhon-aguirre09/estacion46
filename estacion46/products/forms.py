from .models import Product
from bootstrap_modal_forms.forms import BSModalForm

class ProductForm(BSModalForm):

    class Meta:
        model = Product
        exclude = ['fecha']
