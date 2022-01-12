# Encryptor

Project created to encrypt random files using AES, DES or DES3

## Usage

All help related to running the project can be obtained by running the command `python encryptor.py --help`

## Logs
```bash
(.venv) ➜  encryption git:(master) ✗ python encryptor.py -encrypt -a AES                               
Report:
        Encrypted: ./disc_sim/text1.txt
        Key file: ./disc_sim/aes_key_text1.txt
        Output: ./disc_sim/aes_encrypted_text1.txt

Report:
        Encrypted: ./disc_sim/text4.txt
        Key file: ./disc_sim/aes_key_text4.txt
        Output: ./disc_sim/aes_encrypted_text4.txt

Report:
        Encrypted: ./disc_sim/text5.txt
        Key file: ./disc_sim/aes_key_text5.txt
        Output: ./disc_sim/aes_encrypted_text5.txt

Report:
        Encrypted: ./disc_sim/text6.txt
        Key file: ./disc_sim/aes_key_text6.txt
        Output: ./disc_sim/aes_encrypted_text6.txt

Report:
        Encrypted: ./disc_sim/text8.txt
        Key file: ./disc_sim/aes_key_text8.txt
        Output: ./disc_sim/aes_encrypted_text8.txt

Report:
        Encrypted: ./disc_sim/text11.txt
        Key file: ./disc_sim/aes_key_text11.txt
        Output: ./disc_sim/aes_encrypted_text11.txt

Report:
        Encrypted: ./disc_sim/text14.txt
        Key file: ./disc_sim/aes_key_text14.txt
        Output: ./disc_sim/aes_encrypted_text14.txt

Report:
        Encrypted: ./disc_sim/text15.txt
        Key file: ./disc_sim/aes_key_text15.txt
        Output: ./disc_sim/aes_encrypted_text15.txt

Report:
        Encrypted: ./disc_sim/text18.txt
        Key file: ./disc_sim/aes_key_text18.txt
        Output: ./disc_sim/aes_encrypted_text18.txt

Report:
        Encrypted: ./disc_sim/text20.txt
        Key file: ./disc_sim/aes_key_text20.txt
        Output: ./disc_sim/aes_encrypted_text20.txt

(.venv) ➜  encryption git:(master) ✗ cat disc_sim/aes_encrypted_text1.txt 
� eS�^����5��>���|�n��npZ��ia�R��nc�	�k�5u⥠`X=r�Z��xݔ����n��g��7sF0y�JX8rr(��t�
@>K?2A�0%�%�O<��E�d-Ʋ�9J�*rX(��������S '����%t͉���΍� �yI]7R�ӷ��W���������MX��Pk���"B>ט&Wx�.]�iM�5�-^.�$ױ��]�;�`�1L����4����LƚC�Y�����А�mY���6yp�=$�éS�����<��2�6�h]�|u�WԘ��R�$Ҭ�B$�ѱLd\B$�V��
w	��W>��]�Tis;='NXQ`���ex�!nU�B�Y���[�0_t
                                               j��Wίv� g�c���#1�?�|3�ŕQ�7��i
���$��o�\�e�۵z�R!%���{�q�f�0���8uE4�Jط\�L���iT"@��@�X�:�%�q��O��%lԝ�j����C7
��c�̣J�:�řގI)�W���ޫpc���=���K�0(B�헊0~R�X��j*
                                           ���qK�J��IZa$j��?�˼oF���K�;S�[,��lS|7�u�(*�����ٻ��E���0b]��^�r����K��;ʰ������,#j�汑]Ǭ����۱�%������isbs�I�!����' ���Y�ă�����Ѷ��(ߛ���U
z�my�ƿp-��^[s��!�N�M��2OJ
                         �����°9�%�_����{N1��~��h�b׹A������V�̢��|�z'E�N���T"-i�,�7
���.���6���F��X�9���#V-����9�y��܄�;F5a�#�<�
                                           ����1�ډ�Pr砹&R?Ã�x��+ra��
                                                                    S$�=��U���k����"���0�3q_$E{E���A��E0Ž�>�v�}ơ#�Srh ��b�|
                                                                                                                           Y��J�!�Iɀ�6X��Y`y��x�-eΪ�q&5n9�=v./L��W��e�q��Py�5p�o������d��D���8���^�3����֙d���E���A��H
                                                       �cf�`d��(g�փ6��+�p���Ϲ7�[WyF$�S�c��O�S���
                                                                                                3hz�F�	;D$w���	��+��⢊�*����V���K@�ma��
                                                                                                                                       �Z)7:QO��(љ�-T|H�ٟ.��͓��iq6�k�N��~G1�3�Zͫ�o~�UǕN�
                        ��R�یw�Arߓ����>�G6�7���w�Q������0�#�B���ÜH8�sy[1JCv6�����)���ݠ*<�4��S��L�?-�?f|�_���CZ˯Gw(�wW���io�	��o��t���^f����
�y�t�����B�(�q�֜�xz�
                   ��Uw]�Ԥ�p�{���D˵��
�Y&�������J@LJ�(!P�é��a��Coq�~�kf�0�껔X�`�v�Q=�C��i����db�����˙�H�q�=(���jC2*����l	��6��&m�1�^��`	C�M_�nL�MAё��dϗ
                                                                                                                       �[R��q��
@L�w2-Ġ�/r�g���N\�/�z7���n\f49�ud*<�<���R�۫Y#���¬�s�O<�$�d���-Drc��ZelE�
NyI���6�%                                                                                                                                                    (.venv) ➜  encryption git:(master) ✗ 
```


## Used package
[PyCryptodome](https://pypi.org/project/pycryptodome/)
