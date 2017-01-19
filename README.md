# butterfly
butterfly names alignment

THIS ALIGNMENT IS COMPLETE, BUT NOT TESTED. TESTING IN PROGRESS. USE WITH CAUTION.

This is an alignment of Lepidopteran names in four classifications and ten list of names used by monitoring projects.
Classifications
1. ITIS
2. NABA
3. Pelham
4. Opler & Warren

Project Lists
1. Illinois Butterfly Monitoring Network
2. Cascades Butterfly Project
3. Colorado Butterfly Monitoring Network
4. Florida Butterfly Monitoring Network
5. Iowa Butterfly Survey Network
6. Michigan Butterfly Network
7. MPG Ranch Butterfly Monitoring Program
8. Ohio Butterfly Monitoring Network
9. Orange County Butterfly Monitoring Network
10. Tennessee Butterfly Monitoring Network

*Note: Orange County Butterfly Monitoring Network was also known as Irvine Ranch

alignment_test.ipynb is a jupyter notebook to use to test the alignment

starting build for URL: https://github.com/diatomsrcool/butterfly
fetching source at https://github.com/diatomsrcool/butterfly
Step 1 : FROM andrewosh/binder-base:latest
---> 10c75734a0d4
Step 2 : RUN mkdir /home/main/notebooks
---> Running in 03136b501f55
---> 89cb940756b6
Removing intermediate container 03136b501f55
---> Running in 77cf4caf5d62
Step 4 : WORKDIR /home/main/notebooks
Removing intermediate container 77cf4caf5d62
Removing intermediate container 78c7206821bd
Removing intermediate container e71944148bf6
Step 9 : RUN find $HOME/notebooks -name '*.ipynb' -exec jupyter trust {} \;
---> Running in ecf250769856
[91m[TrustNotebookApp] Writing notebook-signing key to /home/main/.local/share/jupyter/notebook_secret[0m
Signing notebook: /home/main/notebooks/alignment_test.ipynb
---> 5136532da3d5
Removing intermediate container ecf250769856
Step 10 : USER main
---> Running in 533bddacd77b
---> 7e4102532ee5
Removing intermediate container 533bddacd77b
Step 11 : WORKDIR $HOME/notebooks
---> Running in c22e33432e90
---> 67cf4a99b190
Removing intermediate container c22e33432e90
Successfully built 67cf4a99b190
registering template for diatomsrcool-butterfly

