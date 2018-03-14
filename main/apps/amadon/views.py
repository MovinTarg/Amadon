# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    if 'tItems' not in req.session:
        req.session['tItems'] = 0
    if 'tPrice' not in req.session:
        req.session['tPrice'] = 0
    if 'quantity' not in req.session:
        req.session['quantity'] = 0
    return render(req, 'amadon/index.html')

def purchase(req):
    
    req.session['quantity'] = req.POST.get('quantity')
    req.session['tItems'] += int(req.session['quantity'])

    if req.POST.get('product_id') == '1001':
        req.session['price'] = 19.99 * int(req.session['quantity'])
    elif req.POST.get('product_id') == '1002':
        req.session['price'] = 29.99 * int(req.session['quantity'])
    elif req.POST.get('product_id') == '1003':
        req.session['price'] = 4.99 * int(req.session['quantity'])
    elif req.POST.get('product_id') == '1004':
        req.session['price'] = 49.99 * int(req.session['quantity'])
    
    req.session['tPrice'] = req.session['tPrice'] + (req.session['price'] * int(req.session['quantity']))

    return redirect('/checkout')

def checkout(req):
    context = {
        'price': req.session['price'],
        'tItems': req.session['tItems'],
        'tPrice': req.session['tPrice'],
    }
    return render(req, 'amadon/checkout.html', context)

def goBack(req):
    return redirect('/')