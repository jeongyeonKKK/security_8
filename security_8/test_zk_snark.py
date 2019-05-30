import zk_snark as zk

pv = zk.prover(2)
AT, BT, CT, HT = pv.QAP()

vf = zk.verifier(4,3,4,5,6)

#1
p_n_a, p_n_b, p_n_c, p_n_h = pv.get_proof_1()
result_1 = vf.verify_1(AT, BT, CT, HT, p_n_a, p_n_b, p_n_c, p_n_h)
print("result_1 = %s", result_1)

#2
p_n_a_2, p_n_b_2, p_n_c_2 = pv.get_proof_2()
result_2 = vf.verify_2(p_n_a_2, p_n_b_2, p_n_c_2)
print("result_2 = %s", result_2)

#3
p_n = pv.get_proof_3()
result_3 = vf.verify_3(p_n)
print("result_3 = %s", result_3)