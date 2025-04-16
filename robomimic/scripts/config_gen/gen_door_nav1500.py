from robomimic.scripts.config_gen.config_gen_utils import *


def make_generator_helper(args):
    algo_name_short = "bc_xfmr"

    generator = get_generator(
        algo_name="bc_xfmr",
        config_file=os.path.join(base_path, 'robomimic/exps/templates/bc_transformer.json'),
        args=args,
        algo_name_short=algo_name_short,
    )

    ### Define dataset variants to train on ###
    generator.add_param(
        key="train.data",
        name="CloseSingleDoor",
        group=123456,
        values_and_names=[
            (get_robocasa_ds("CloseSingleDoor", src="mg_nav_fixview", eval=[],
                             filter_key="1500_demos"), "mg-1500-nav")
        ]
    )

    generator.add_param(
        key="train.output_dir",
        name="",
        group=-1,
        values=[get_output_dir(args, algo_dir=algo_name_short + "_nav")]
    )

    return generator

if __name__ == "__main__":
    parser = get_argparser()

    args = parser.parse_args()
    make_generator(args, make_generator_helper)
