# Starting ITSDAQ

This is where we will discuss what happens when you start ITSDAQ.

## Setting Environmental Variables

Environmental variables are very important. ITSDAQ will not start up if some
are missing and database interactions will also not work properly.

You will need to run two instances of ITSDAQ when thermal cycling, so we will
create two different setup files to use for the various applications.

## Start ITSDAQ

This part is easy, provided the **proper steps** have been followed. Enter the following
after the setup files have been created and sourced:

```
./RUNITSDAQ.sh
```

# Startup Explained

There is a significant amount of output that appears upon startup. You may be
reasonably wondering what it all means. I will attempt to highlight the
important bits so you have somewhere to turn in the event of an issue.
