---
title: The simplest useful computer program
subtitle: A theorem blurs the line between an environment and a programming language
author: Osvaldo
date: '2017-11-10'
slug: the-simplest-useful-computer-program
headerimg: /img/alps.jpg
categories:
  - programming
tags:
  - fundamentals
  - software development
---
*Attention conservation notice:* a few hundred words on the building blocks of
most programming languages. If you can code, you probably know this already. If
you can't code, you probably don't care.

## Motivation

You might have heard of the [Hello, World!](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
program before, a very simple program whose only task is to print _Hello, World!_.

Being so simple, it is often used to show the syntax of a programming language, at least at a very basic level.
On the other hand, being so "useless", a complete newbie wouldn't get a very concrete idea of a computer program
and would even start questioning computer programming as a whole!

So, let's try to write a program that exposes the fundamental building blocks of programming, but is at the same time
very simple and yet somehow useful. We will be writing the code blocks in the most common Linux shell, the Bourne
again shell, better known as _bash_ (more on this later).

### Sequence

The first idea to grasp is the **sequence**. A program, not surprisingly, is executed one instruction after the other.

```
#!/bin/bash

echo "Hello, World!"
echo "My name is Joe."
echo "Goodbye, World!"
```

Here, the first line (the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) ) is used to specify that the program
is written in bash, while `echo` is the command that prints the following to screen. The output of this program is, as
you might expect,

```
Hello, World!
My name is Joe.
Goodbye, World!
```

It would be inconvenient to say goodbye before even saying hello...

### Iteration

Another ingredient is the **iteration**: as long as some condition holds true, keep doing what you are doing.
In order to show a concrete example, let's imagine the following situation. A colleague of yours took about a
hundred photos to document some construction work that is taking place close at your office. When you save them
on your computer, their naming is something like `DSC3162.jpg`, `DSC3163.jpg`, `DSC3164.jpg` and so on up to
`DSC3271.jpg`.
You would like to have a more transparent scheme, like `Baustelle_1.jpg`, `Baustelle_2.jpg` and so on. Is there
a way to do this automatically, rather than renaming them one by one? It turns
out that these few lines do the trick. Comments appearing after \# do not
affect the program and are written only to explain in common language what each line does.
The command `mv old_name new_name` is used to rename files.

```
#!/bin/bash

i=3162  # start from 3162
while (( $i <= 3271 ))  # repeat lines between do and done, but stop at 3271
do
  j=$(( i-3161 ))  # renamed photos start from 1 (3162 - 3161 = 1)
	mv "DSC${i}.jpg" "Baustelle_${j}.jpg"  # rename DSC3162.jpg to Baustelle_1.jpg
	i=$(( i+1 ))  # go to next photo
done
```

In these few lines we have also introduced a convenient entity called **variable**.
These are containers that are used throughout a program to store some information
that is needed in different parts of the program. At the beginning we have set
the variable `i` to 3162 (remember that the first photo we want to rename is
`DSC3162.jpg`). After renaming of each file we increment this variable by one
with the instruction `i=$(( i+1 ))` in order to deal with the next photo.

### Selection

Let's now add a third ingredient: the selection. In plain language, do this or that
based on whether a condition is true or not.
Let's elaborate on the previous example. After taking photos of the construction site,
your colleague uses the same camera to take about two hundred photos at the Christmas party.
Original files will follow the same naming scheme, meaning that files `DSC3272.jpg` to `DSC3498.jpg`
should be renamed `Xmas_party_2017_1.jpg`, `Xmas_party_2017_2.jpg`... In code:

```
#!/bin/bash

i=3162  # start from 3162
while (( $i <= 3498 ))  # rename all photos up to DSC3498.jpg
do
  if (("$i" <= 3271)); then  # the first set of photos follows the old rule
     j=$(( i-3161 ))
	   mv "DSC${i}.jpg" "Baustelle_${j}.jpg"
   else  # the second set is renamed to Xmas_party_2017_...
     j=$(( i-3271 ))  # party photos should also start from 1 (3272 - 3271 = 1)
     mv "DSC${i}.jpg" "Xmas_party_2017_${j}.jpg"
   fi
	i=$(( i+1 ))  # go to next photo
done
```

## Defining a programming language

Choosing exactly these three building blocks was not arbitrary. According to the
Böhm-Jacopini theorem, appeared in a journal in 1966, these ingredients allow to
write any algorithm. This result is also called _structured program theorem_,
and I first [learned about it](http://lca.dii.unisalento.it/download/comunix.pdf)
during my studies in physics when I started to use Unix/Linux shells.
These shells are the environment provided to the user by these operating systems,
and anyone who has used them least once will recognize their distinctive feature:
they are at the same time an environment and a programming language able to perform
even the most complex operation. This makes them so powerful (and dangerous) that inspired some
to draw an analogy between Unix and
[chainsaws](http://www.vincebuffalo.com/blog/2013/08/08/using-names-pipes-and-process-substitution-in-bioinformatics.html).


_Corrado Böhm, aged 94, died last 23 October._
