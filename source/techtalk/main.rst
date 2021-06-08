#########
techtalks
#########

.. toctree::
   :maxdepth: 5

************
open markets
************


the space race for open finance
===============================

the why
-------

Big markets, big bullshit
Obfuscating collateral, hidden risk

Banks plebs and psychology
Banks plebs and lemons

How do markets work?
How can we make this more transparent?

cons in tradfi
- 


promises promises
-----------------

crypto:
 - power of incorruptible collateral
 - verify without rating agencies/banks
 - non-custodial wallets

reality:
 - CeFi cascades of `doom`_
   who got `rekt today`?
 - `MEV`_ (Miner Extractable Value)
   miners can determine the order of when transactions are processed, mempool

.. image:: picture.jpg
   :width: 200px
   :height: 100px
   :scale: 50 %
   :alt: alternate text
   :align: right

 - gazmataz
   `example ethereum`
 - shitcoins memecoins

.. _doom: https://cointelegraph.com/news/cointelegraph-consulting-defi-hit-by-a-tsunami-of-liquidations-in-may
.. _rekt today: https://app.rek.to/
.. _MEV: https://blog.chain.link/what-is-miner-extractable-value-mev/
.. _example ethereum: https://etherscan.io/gastracker

got stopped out?
verify what happened = difference with cefi

vega can't put in a stop order
check github discussions on that (obfuscation stuff)
vega is an orderbook exchange initially later amm style
key: target liquidity level
liquidityprovider:  incentivized liquidity protection, share price price, stop providing liquidity = loose share. Dig into liquidity protection

it is not just about swapping tokens :)
trade data
might be the weather!

vega is looking at perpetuals, hourly perpetuals

deriviatives = set of rules of how you gonna swap assets under various conditions in the future

ssl example

.. code::

   curl -vvI https://www.reddit.com/search/?q=paypal%20block

   *   Trying 151.101.37.140:443...
   * TCP_NODELAY set
   * Connected to www.reddit.com (151.101.37.140) port 443 (#0)
   * ALPN, offering h2
   * ALPN, offering http/1.1
   * successfully set certificate verify locations:
   *   CAfile: /etc/ssl/certs/ca-certificates.crt
     CApath: /etc/ssl/certs
   * TLSv1.3 (OUT), TLS handshake, Client hello (1):
   * TLSv1.3 (IN), TLS handshake, Server hello (2):
   * TLSv1.2 (IN), TLS handshake, Certificate (11):
   * TLSv1.2 (IN), TLS handshake, Server key exchange (12):
   * TLSv1.2 (IN), TLS handshake, Server finished (14):
   * TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
   * TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
   * TLSv1.2 (OUT), TLS handshake, Finished (20):
   * TLSv1.2 (IN), TLS handshake, Finished (20):
   * SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
   * ALPN, server accepted to use h2
   * Server certificate:
   *  subject: C=US; ST=CALIFORNIA; L=SAN FRANCISCO; O=Reddit Inc.; CN=*.reddit.com
   *  start date: May 23 00:00:00 2021 GMT
   *  expire date: Nov 18 23:59:59 2021 GMT
   *  subjectAltName: host "www.reddit.com" matched cert's "*.reddit.com"
   *  issuer: C=US; O=DigiCert Inc; CN=DigiCert TLS RSA SHA256 2020 CA1
   *  SSL certificate verify ok.
   * Using HTTP2, server supports multi-use
   * Connection state changed (HTTP/2 confirmed)
   * Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
   * Using Stream ID: 1 (easy handle 0x55f8f2c2ee10)
   > HEAD /search/?q=paypal%20block HTTP/2
   > Host: www.reddit.com
   > user-agent: curl/7.68.0
   > accept: */*
   > 
   * Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
   < HTTP/2 429 
   HTTP/2 429 
   < content-type: text/html; charset=UTF-8
   content-type: text/html; charset=UTF-8
   < x-ua-compatible: IE=edge
   x-ua-compatible: IE=edge
   < retry-after: 5
   retry-after: 5
   < x-frame-options: SAMEORIGIN
   x-frame-options: SAMEORIGIN
   < x-content-type-options: nosniff
   x-content-type-options: nosniff
   < x-xss-protection: 1; mode=block
   x-xss-protection: 1; mode=block
   < cache-control: max-age=0, must-revalidate
   cache-control: max-age=0, must-revalidate
   < x-moose: majestic
   x-moose: majestic
   < accept-ranges: bytes
   accept-ranges: bytes
   < date: Tue, 08 Jun 2021 06:54:15 GMT
   date: Tue, 08 Jun 2021 06:54:15 GMT
   < via: 1.1 varnish
   via: 1.1 varnish
   < vary: accept-encoding
   vary: accept-encoding
   < set-cookie: loid=0000000000clhaklhm.2.1623135255310.Z0FBQUFBQmd2eFFYRGJJV3RsWFA4aWJ4djlOXzdLV2o5eXh0bFNFZ1A4SDBpZXJiWUhpTktUR3dRUUJQc19LQVJuVnh1N1RwT2hHZGsyUEdqWXNzTllRVVdrNGNYVUVMOWpTT0V4eDFjekZjNzQ2RnFtbjZDQlB4LWhlYlFvT0dWeDRsV1BnZU01NzM; Domain=reddit.com; Max-Age=63071999; Path=/; expires=Thu, 08-Jun-2023 06:54:15 GMT; secure; SameSite=None; Secure
   set-cookie: loid=0000000000clhaklhm.2.1623135255310.Z0FBQUFBQmd2eFFYRGJJV3RsWFA4aWJ4djlOXzdLV2o5eXh0bFNFZ1A4SDBpZXJiWUhpTktUR3dRUUJQc19LQVJuVnh1N1RwT2hHZGsyUEdqWXNzTllRVVdrNGNYVUVMOWpTT0V4eDFjekZjNzQ2RnFtbjZDQlB4LWhlYlFvT0dWeDRsV1BnZU01NzM; Domain=reddit.com; Max-Age=63071999; Path=/; expires=Thu, 08-Jun-2023 06:54:15 GMT; secure; SameSite=None; Secure
   < set-cookie: session_tracker=Pbpr8DDPWUwkRPyT5F.0.1623135255310.Z0FBQUFBQmd2eFFYaVYzWEhXR1BERzg4OWpJSmVhNnB2dHM3dWRVM0NibU5fUDZEbjVMYk9WZXNDYzQ0QzJ2MjZrWjhOcVM4eVFJUkR6MTRucWdGWWRpWEMxM19xTnVCMlVfMnd1Z1hYRjg4cEcwSzBfUUxVbk5XS2J0eUhKaDBrWUZpcHRTLVczSGU; Domain=reddit.com; Max-Age=7199; Path=/; expires=Tue, 08-Jun-2021 08:54:15 GMT; secure; SameSite=None; Secure
   set-cookie: session_tracker=Pbpr8DDPWUwkRPyT5F.0.1623135255310.Z0FBQUFBQmd2eFFYaVYzWEhXR1BERzg4OWpJSmVhNnB2dHM3dWRVM0NibU5fUDZEbjVMYk9WZXNDYzQ0QzJ2MjZrWjhOcVM4eVFJUkR6MTRucWdGWWRpWEMxM19xTnVCMlVfMnd1Z1hYRjg4cEcwSzBfUUxVbk5XS2J0eUhKaDBrWUZpcHRTLVczSGU; Domain=reddit.com; Max-Age=7199; Path=/; expires=Tue, 08-Jun-2021 08:54:15 GMT; secure; SameSite=None; Secure
   < set-cookie: csv=1; Max-Age=63072000; Domain=.reddit.com; Path=/; Secure; SameSite=None
   set-cookie: csv=1; Max-Age=63072000; Domain=.reddit.com; Path=/; Secure; SameSite=None
   < set-cookie: edgebucket=kaModUrAuC4Jaj8L9A; Domain=reddit.com; Max-Age=63071999; Path=/;  secure
   set-cookie: edgebucket=kaModUrAuC4Jaj8L9A; Domain=reddit.com; Max-Age=63071999; Path=/;  secure
   < strict-transport-security: max-age=15552000; includeSubDomains; preload
   strict-transport-security: max-age=15552000; includeSubDomains; preload
   < server: snooserv
   server: snooserv
   < x-clacks-overhead: GNU Terry Pratchett
   x-clacks-overhead: GNU Terry Pratchett
   < content-length: 1064
   content-length: 1064

   < 
   * Connection #0 to host www.reddit.com left intact


shitcoins & rug pulls
*********************
some other talk
***************
**************
time to choose
**************
Vega or Bitmex?

here for open markets: https://linktr.ee/vegaprotocol

here to get rekt on bitmex

*********
demo time
*********
vega
====

api howto
---------

api howto guide

watching the mempool
https://www.blocknative.com/blog/explorer
