Summary:	Shorten - fast compression for waveform files
Summary(pl):	Shorten - szybka kompresja plik�w ze spr�bkowanym d�wi�kiem
Name:		shorten
Version:	2.3a
Release:	1
License:	non-commercial distribution and encoding
Group:		Applications/Sound
Source0:	http://www.hornig.net/files/shorten/linux/source/%{name}-%{version}.tar.gz
# Source0-md5:	c538eeced847c7e231759301b6c10d2f
URL:		http://www.hornig.net/shorten.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shorten provides compression for waveform files, such as RIFF WAVE
(.wav). Both lossless and lossy compression is supported at about 2:1
compression in the lossless case and up to 5:1 compression in the
lossy case.

%description -l pl
Shorten kompresuje pliki ze spr�bkowanym d�wi�kiem, takie jak RIFF
WAVE (.wav). Obs�ugiwana jest zar�wno bezstratna jak i stratna
kompresja ze wsp�czynnikiem oko�o 2:1 w przypadku kompresji
bezstratnej i 5:1 w przypadku stratnej.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install shorten $RPM_BUILD_ROOT%{_bindir}
install shorten.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE tr156.ps
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*