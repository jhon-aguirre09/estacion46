from .models import Inventory
from bootstrap_modal_forms.forms import BSModalForm

class InventoryForm(BSModalForm):

    class Meta:
        model = Inventory
        exclude = ['fecha_Ingreso']
