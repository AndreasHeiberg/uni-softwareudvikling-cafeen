from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'create_product_group': True,
        'update_product_group': True,
        'delete_product_group': True,
        'view_product_group': True,
        'create_product': True,
        'update_product': True,
        'update_product_count': True,
        'delete_product': True,
        'view_product': True,
        'rent_out_product': True,
    }

class BoardMember(AbstractUserRole):
    available_permissions = {
        'view_product_group': True,
        'update_product_count': True,
        'view_product': True,
        'rent_out_product': True,
    }

class KeyCarrier(AbstractUserRole):
    available_permissions = {
        'view_product_group': True,
        'update_product_count': True,
        'view_product': True,
        'rent_out_product': True,
    }