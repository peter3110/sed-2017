#include <random>
#include <string>

#include "message.h"
#include "parsimu.h"
#include "real.h"
#include "tuple_value.h"

#include "FplusInf.h"

using namespace std;

FplusInf::FplusInf(const string &name) :
	Atomic(name),
	inVar1(addInputPort("inVar1")),
	inVar2(addInputPort("inVar2")),
	out(addOutputPort("out")),
	var1(1),
	var2(1),
	val(1)
{
}


Model &FplusInf::initFunction()
{
	holdIn(AtomicState::passive, VTime::Inf);
	return *this;
}


Model &FplusInf::externalFunction(const ExternalMessage &msg)
{
	double f = 0.5;
	double x = Tuple<Real>::from_value(msg.value())[0].value();

	if(msg.port() == inVar1) {
		var1 = x;
	} else if (msg.port() == inVar2) {
		var2 = x;
	}
	holdIn(AtomicState::active, VTime::Zero);
	return *this;
}


Model &FplusInf::internalFunction(const InternalMessage &)
{
	passivate();
	return *this ;
}


Model &FplusInf::outputFunction(const CollectMessage &msg)
{
	double contact_infectivity = 0.3;
	double total_population = 1000;
	double val2 = (var1 * var2) / (contact_infectivity * total_population);

	Tuple<Real> out_value { val2 };
	sendOutput(msg.time(), out, out_value);

	return *this ;
}
