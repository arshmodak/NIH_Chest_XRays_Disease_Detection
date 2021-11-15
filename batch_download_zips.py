#!/usr/bin/env python3
# Download the 56 zip files in Images_png in batches
import urllib.request
import tarfile
import time

# URLs for the zip files
links = [
    'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
    'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
    'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz',
	'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
    'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
	'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
	'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
    'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
	'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
	'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
	'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
	'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz'
]

def extract_tar(filename):
    if filename.endswith("tar.gz"):
        tar = tarfile.open(filename, "r:gz")
        tar.extractall()
        tar.close()
    # elif fname.endswith("tar"):
    #     tar = tarfile.open(fname, "r:")
    #     tar.extractall()
    #     tar.close()

    print("Extraction of {} complete".format(filename))



    return


for idx, link in enumerate(links):
    # time.sleep(2)
    path = r"E:\ARSH\NEU\Fall 2021\CS 5100\Projects\Data\Images"
    fn = r"{}\images_{:02d}.tar.gz".format(path, idx+1)
    print('Downloading {}: {}...'.format(idx+1, link))
    urllib.request.urlretrieve(link, fn)  # download the zip file
    extract_tar(fn)

    # break

print("Download complete. Please check the checksums")

