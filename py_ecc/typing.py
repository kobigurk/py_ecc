from typing import (
    Tuple,
    TypeVar,
    Union,
)

from py_ecc.fields import (
    gmp_optimized_bn128_FQ,
    gmp_optimized_bn128_FQP,
    gmp_optimized_bn128_FQ2,
    gmp_optimized_bn128_FQ12,
)
from py_ecc.fields.gmp_optimized_field_elements import (
    FQ as Optimized_FQ,
    FQP as Optimized_FQP,
    FQ2 as Optimized_FQ2,
    FQ12 as Optimized_FQ12,
)


#
# These types are wrt Normal Integers
#
PlainPoint2D = Tuple[int, int]
PlainPoint3D = Tuple[int, int, int]


#
# Types for the normal curves and fields
#
Field = TypeVar(
    'Field',
    # General
    # bn128
    gmp_optimized_bn128_FQ,
    gmp_optimized_bn128_FQP,
    gmp_optimized_bn128_FQ2,
    gmp_optimized_bn128_FQ12,
)
Point2D = Tuple[Field, Field]
Point3D = Tuple[Field, Field, Field]
GeneralPoint = Union[Point2D[Field], Point3D[Field]]


#
# Types For optimized curves and fields
#
Optimized_Field = TypeVar(
    'Optimized_Field',
    # General
    Optimized_FQ,
    Optimized_FQP,
    Optimized_FQ2,
    Optimized_FQ12,
    # bn128
    gmp_optimized_bn128_FQ,
    gmp_optimized_bn128_FQP,
    gmp_optimized_bn128_FQ2,
    gmp_optimized_bn128_FQ12,
    # bls12_381
)
Optimized_Point2D = Tuple[Optimized_Field, Optimized_Field]
Optimized_Point3D = Tuple[Optimized_Field, Optimized_Field, Optimized_Field]
Optimized_GeneralPoint = Union[
    Optimized_Point2D[Optimized_Field],
    Optimized_Point3D[Optimized_Field],
]

#
# Miscellaneous types
#
FQ2_modulus_coeffs_type = Tuple[int, int]
FQ12_modulus_coeffs_type = Tuple[int, int, int, int, int, int, int, int, int, int, int, int]
