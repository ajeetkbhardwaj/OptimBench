"""CEC (Real-World Multiobjective) benchmark functions for optimization algorithms."""

# RW-MOP-2021 problem exports - imported from individual modules
from .pressure_vessal import pressure_vessal
from .vibrating_platform import vibrating_platform
from .two_bar_Truss_design_problems import two_bar_Truss_design_problems
from .weldan_beam_design import weldan_beam_design
from .disc_brake_design import disc_brake_design
from .speed_reducer_design import speed_reducer_design
from .gear_train_design import gear_train_design
from .car_side_impact_design import car_side_impact_design
from .four_bar_plane_truss import four_bar_plane_truss
from .two_bar_plane_truss import two_bar_plane_truss
from .water_tesource_management import water_tesource_management
from .simply_supported_I_beam_design import simply_supported_I_beam_design
from .gear_box_design import gear_box_design
from .multiple_disk_clutch_brake_design import multiple_disk_clutch_brake_design
from .spring_design import spring_design
from .cantilever_beam_design import cantilever_beam_design
from .bulk_carriers_design import bulk_carriers_design
from .front_rail_design import front_rail_design
from .multi_product_batch_plant import multi_product_batch_plant
from .hydro_static_thrust_bearing_design import hydro_static_thrust_bearing_design
from .crash_energy_management_for_high_speed_train import crash_energy_management_for_high_speed_train

__all__ = [
    "pressure_vessal",
    "vibrating_platform",
    "two_bar_Truss_design_problems",
    "weldan_beam_design",
    "disc_brake_design",
    "speed_reducer_design",
    "gear_train_design",
    "car_side_impact_design",
    "four_bar_plane_truss",
    "two_bar_plane_truss",
    "water_tesource_management",
    "simply_supported_I_beam_design",
    "gear_box_design",
    "multiple_disk_clutch_brake_design",
    "spring_design",
    "cantilever_beam_design",
    "bulk_carriers_design",
    "front_rail_design",
    "multi_product_batch_plant",
    "hydro_static_thrust_bearing_design",
    "crash_energy_management_for_high_speed_train",
]