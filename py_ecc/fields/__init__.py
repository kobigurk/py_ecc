from .field_elements import (
    FQ,
    FQP,
    FQ2,
    FQ12,
)

from .field_properties import (
    field_properties,
)

from .gmp_optimized_field_elements import (
    FQ as gmp_optimized_FQ,
    FQP as gmp_optimized_FQP,
    FQ2 as gmp_optimized_FQ2,
    FQ12 as gmp_optimized_FQ12,
)

import gmpy2
from gmpy2 import mpz
#
# optimized_bn128 curve fields
#

class gmp_optimized_bn128_FQ(gmp_optimized_FQ):
    field_modulus = mpz(field_properties["bn128"]["field_modulus"])

class gmp_optimized_bn128_FQP(gmp_optimized_FQP):
    field_modulus = mpz(field_properties["bn128"]["field_modulus"])


class gmp_optimized_bn128_FQ2(gmp_optimized_FQ2, gmp_optimized_bn128_FQP):
    field_modulus = mpz(field_properties["bn128"]["field_modulus"])
    FQ2_MODULUS_COEFFS = field_properties["bn128"]["fq2_modulus_coeffs"]


class gmp_optimized_bn128_FQ12(gmp_optimized_FQ12, gmp_optimized_bn128_FQP):
    field_modulus = mpz(field_properties["bn128"]["field_modulus"])
    FQ12_MODULUS_COEFFS = field_properties["bn128"]["fq12_modulus_coeffs"]
