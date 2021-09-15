# ConsistentColorsProject
Facilities to easily import some matplotlib color schemes in mathematica and adobe illustrator. The supported color scemes are a Tiny subset of matplotlibs entire library. 

## Using the mathematica module

In order to be able to import `pythonColors.m` you will have to install the package first. This can be done using mathematica notebooks gui. This method is described [here](https://support.wolfram.com/5648?src=mathematica).
However a simpler method that I prefer is to simply copy the file in the proper import directory where mathematica looks for modules. The position of this folder can be found by printing out the variable `$BaseDirectory` or `$UserBaseDirectory`. Copying the file in the first directory will install it for all users and might require root access and copying it into the second will only instqall the file for the current user.
Then the modeule can be imported like so:
```mathematica
<< "pythonColors.m"
```
