#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-whoami
Version  : 1.2.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/whoami_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/whoami_1.2.0.tar.gz
Summary  : Username, Full Name, Email Address, 'GitHub' Username of the
Group    : Development/Tools
License  : MIT
Requires: R-cli
BuildRequires : R-cli
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
# whoami
[![Linux Build Status](https://travis-ci.org/r-lib/whoami.svg?branch=master)](https://travis-ci.org/r-lib/whoami)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/r-lib/whoami?svg=true)](https://ci.appveyor.com/project/gaborcsardi/whoami)
[![](http://www.r-pkg.org/badges/version/whoami)](http://www.r-pkg.org/pkg/whoami)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/whoami)](http://www.r-pkg.org/pkg/whoami)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/whoami/master.svg)](https://codecov.io/github/r-lib/whoami?branch=master)

%prep
%setup -q -c -n whoami

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552837911

%install
export SOURCE_DATE_EPOCH=1552837911
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whoami
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whoami
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library whoami
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  whoami || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/whoami/DESCRIPTION
/usr/lib64/R/library/whoami/INDEX
/usr/lib64/R/library/whoami/LICENSE
/usr/lib64/R/library/whoami/Meta/Rd.rds
/usr/lib64/R/library/whoami/Meta/features.rds
/usr/lib64/R/library/whoami/Meta/hsearch.rds
/usr/lib64/R/library/whoami/Meta/links.rds
/usr/lib64/R/library/whoami/Meta/nsInfo.rds
/usr/lib64/R/library/whoami/Meta/package.rds
/usr/lib64/R/library/whoami/NAMESPACE
/usr/lib64/R/library/whoami/NEWS.md
/usr/lib64/R/library/whoami/R/whoami
/usr/lib64/R/library/whoami/R/whoami.rdb
/usr/lib64/R/library/whoami/R/whoami.rdx
/usr/lib64/R/library/whoami/README.md
/usr/lib64/R/library/whoami/help/AnIndex
/usr/lib64/R/library/whoami/help/aliases.rds
/usr/lib64/R/library/whoami/help/paths.rds
/usr/lib64/R/library/whoami/help/whoami.rdb
/usr/lib64/R/library/whoami/help/whoami.rdx
/usr/lib64/R/library/whoami/html/00Index.html
/usr/lib64/R/library/whoami/html/R.css
/usr/lib64/R/library/whoami/tests/testthat.R
/usr/lib64/R/library/whoami/tests/testthat/test-email.R
/usr/lib64/R/library/whoami/tests/testthat/test-fallbacks.R
/usr/lib64/R/library/whoami/tests/testthat/test-fullname.R
/usr/lib64/R/library/whoami/tests/testthat/test-gh-username.R
/usr/lib64/R/library/whoami/tests/testthat/test-memoize.R
/usr/lib64/R/library/whoami/tests/testthat/test-username.R
