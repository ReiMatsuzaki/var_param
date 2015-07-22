

utest1:
	python test/test1/test1.py 
	echo "-------------------------"
	ls test/test1/results/

utest1_clear:
	rmdir test/test1/results/_1.0_SCF
	rmdir test/test1/results/_2.0_DFT

utest2:
	python test/test2/test2.py

utest_param:
	python test/test_params/test.py

test_opt_cbf:
	python test/test_opt_cbf/test_opt_cbf.py

test_opt_cbf_extract:
	python test/test_opt_cbf/extract.py
