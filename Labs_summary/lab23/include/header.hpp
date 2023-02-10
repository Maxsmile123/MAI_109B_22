#ifndef HEADER.HPP
#define HEADER.HPP


class Lol{
	public:
		explicit Lol(int _a);
		~Lol();
		int get_a() const;
		char* get_string() const;	


private:
		int a = 15;
		char* string = nullptr;

};

#endif // HEADER.HPP
