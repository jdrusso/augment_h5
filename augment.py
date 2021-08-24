import h5py
from shutil import copyfile

source_h5 = "/Users/russojd/Research/wca_dimer/westpa_tutorials/basic_nacl/west.h5"

crawl_aux = "augment_data.h5"
dest_h5 = "west_augmented.h5"


def augment_h5():
    """
    Copy iteration auxdata from iter_XXX/auxdata/coord in crawl_aux to dest_h5.

    Copies source_h5 to dest_h5 to avoid writing to the original WESTPA h5 file.
    """

    dataset_to_copy = "coord"

    # First, make a new file to avoid corrupting main h5 file
    copyfile(source_h5, dest_h5)

    # goal is to copy over each iteration aux data from crawl to west
    west_h5 = h5py.File(dest_h5, mode="r+")
    crawl_h5 = h5py.File(crawl_aux, mode="r")

    # copies over all iterations available on the crawl h5 dataset
    for iter in range(1, crawl_h5.attrs["iter_stop"]):

        auxdata_path = f"iterations/iter_{iter:08d}/auxdata"

        try:
            west_h5.create_group(auxdata_path)
        except ValueError:
            # If auxdata group already exists, do nothing
            pass

        crawl_h5.copy(f"{auxdata_path}/{dataset_to_copy}", west_h5[auxdata_path])


if __name__ == "__main__":

    augment_h5()
